// Industrial Boredom Button v2.0

class BoredomDestructionSystem {
    constructor() {
        this.activityCount = 0;
        this.totalMinutes = 0;
        this.currentCategory = 'all';
        this.currentTheme = document.body.dataset.theme || 'light';
        this.init();
    }

    init() {
        this.bindEvents();
        this.loadInitialData();
        this.updateSystemStats();
        this.setupSound();
    }

    bindEvents() {
        // Main Button
        document.getElementById('industrialBtn').addEventListener('click', () => {
            this.generateActivity();
            this.playIndustrialSound();
        });

        // Category Filters
        document.querySelectorAll('.category-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.selectCategory(e.target.dataset.category);
            });
        });

        // Theme Toggle
        document.getElementById('themeToggle').addEventListener('click', () => {
            this.toggleTheme();
        });

        // Skip Button
        document.getElementById('skipBtn')?.addEventListener('click', () => {
            this.skipActivity();
        });
    }

    async generateActivity() {
        try {
            // Show loading state
            this.showLoading(true);
            
            // Get activity from API
            const url = this.currentCategory === 'all' 
                ? '/random' 
                : `/random?category=${this.currentCategory}`;
            
            const response = await fetch(url);
            const data = await response.json();
            
            // Update display
            this.updateActivityDisplay(data.activity);
            
            // Update stats
            this.updateStats(data.activity.duration);
            
            // Update system stats
            this.updateSystemStats();
            
            // Add mechanical animation
            this.mechanicalAnimation();
            
        } catch (error) {
            console.error('System Error:', error);
            this.showError();
        } finally {
            this.showLoading(false);
        }
    }

    updateActivityDisplay(activity) {
        const display = document.getElementById('activityDisplay');
        
        display.innerHTML = `
            <div class="activity-content">
                <div class="activity-icon">${activity.icon}</div>
                <div class="activity-name">${activity.name}</div>
                <div class="activity-meta">
                    <div class="meta-tag">
                        ${this.getCategoryIcon(activity.category)} ${this.getCategoryName(activity.category)}
                    </div>
                    <div class="meta-tag">⏱️ ${activity.duration} MIN</div>
                    <div class="meta-tag">⚡ ${activity.intensity?.toUpperCase() || 'MEDIUM'}</div>
                </div>
            </div>
        `;
        
        // Add animation
        display.classList.add('new-output');
        setTimeout(() => display.classList.remove('new-output'), 500);
    }

    updateStats(duration) {
        this.activityCount++;
        this.totalMinutes += parseInt(duration) || 5;
        
        document.getElementById('activityCount').textContent = this.activityCount;
        document.getElementById('totalMinutes').textContent = this.totalMinutes;
        
        // Update efficiency
        const efficiency = Math.min(100, Math.floor(this.activityCount * 6.66));
        document.getElementById('systemEfficiency').textContent = `${efficiency}%`;
    }

    async updateSystemStats() {
        try {
            const response = await fetch('/system-stats');
            const data = await response.json();
            
            // Randomize some stats for realism
            document.getElementById('sysPressure').textContent = 
                `${Math.floor(80 + Math.random() * 20)} PSI`;
            document.getElementById('sysTemperature').textContent = 
                `${Math.floor(20 + Math.random() * 15)}°C`;
            document.getElementById('sysEfficiency').textContent = 
                `${Math.floor(85 + Math.random() * 14)}%`;
                
        } catch (error) {
            console.log('Stats update failed:', error);
        }
    }

    selectCategory(category) {
        this.currentCategory = category;
        
        // Update UI
        document.querySelectorAll('.category-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.category === category);
        });
        
        // Generate activity from new category
        this.generateActivity();
    }

    toggleTheme() {
        this.currentTheme = this.currentTheme === 'light' ? 'dark' : 'light';
        document.body.dataset.theme = this.currentTheme;
        
        // Save preference
        localStorage.setItem('industrialTheme', this.currentTheme);
        
        // Update toggle position
        const toggle = document.getElementById('themeToggle');
        toggle.querySelector('.shift-label').textContent = 
            this.currentTheme === 'light' ? 'DAY SHIFT' : 'NIGHT SHIFT';
    }

    showLoading(show) {
        const button = document.getElementById('industrialBtn');
        const loadingGears = document.getElementById('loadingGears');
        
        if (show) {
            button.disabled = true;
            button.innerHTML = '<span class="button-icon">⚙️</span>PROCESSING...';
            if (loadingGears) loadingGears.style.display = 'flex';
        } else {
            button.disabled = false;
            button.innerHTML = '<span class="button-icon">⚡</span>ENGAGE SYSTEMS';
            if (loadingGears) loadingGears.style.display = 'none';
        }
    }

    mechanicalAnimation() {
        // Add conveyor belt animation
        const monitor = document.querySelector('.activity-monitor');
        monitor.style.animation = 'none';
        setTimeout(() => {
            monitor.style.animation = 'conveyor 0.5s linear';
        }, 10);
        
        // Gear animation
        const gears = document.querySelectorAll('.gear');
        gears.forEach(gear => {
            gear.style.animation = 'none';
            setTimeout(() => {
                gear.style.animation = 'gearSpin 2s linear infinite';
            }, 10);
        });
    }

    playIndustrialSound() {
        // Create mechanical sound effect
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        
        oscillator.frequency.setValueAtTime(100, audioContext.currentTime);
        oscillator.frequency.exponentialRampToValueAtTime(400, audioContext.currentTime + 0.1);
        
        gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.3);
        
        oscillator.start();
        oscillator.stop(audioContext.currentTime + 0.3);
    }

    setupSound() {
        // Initialize Web Audio API
        if (!window.AudioContext && !window.webkitAudioContext) {
            console.log('Web Audio API not supported');
        }
    }

    getCategoryIcon(category) {
        const icons = {
            'olahraga': '💪',
            'produktivitas': '🏭',
            'kesehatan': '❤️',
            'kreatif': '🔬',
            'edukasi': '🎓',
            'sosial': '👥',
            'skill': '⚡',
            'all': '⚙️'
        };
        return icons[category] || '⚙️';
    }

    getCategoryName(category) {
        const names = {
            'olahraga': 'PHYSICAL MAINTENANCE',
            'produktivitas': 'PRODUCTION LINE',
            'kesehatan': 'SYSTEM HEALTH',
            'kreatif': 'R&D DEPARTMENT',
            'edukasi': 'TRAINING MODULE',
            'sosial': 'TEAM SYNCING',
            'skill': 'SKILL UPGRADE',
            'all': 'ALL SYSTEMS'
        };
        return names[category] || category.toUpperCase();
    }

    showError() {
        const display = document.getElementById('activityDisplay');
        display.innerHTML = `
            <div class="activity-content">
                <div class="activity-icon">⚠️</div>
                <div class="activity-name">SYSTEM MALFUNCTION</div>
                <div class="activity-meta">
                    <div class="meta-tag">🔧 MAINTENANCE REQUIRED</div>
                    <div class="meta-tag">🔄 TRY AGAIN</div>
                </div>
            </div>
        `;
    }

    skipActivity() {
        // Quick skip with animation
        document.getElementById('activityDisplay').style.opacity = '0.5';
        setTimeout(() => {
            this.generateActivity();
            document.getElementById('activityDisplay').style.opacity = '1';
        }, 300);
    }

    loadInitialData() {
        // Load saved theme
        const savedTheme = localStorage.getItem('industrialTheme');
        if (savedTheme) {
            this.currentTheme = savedTheme;
            document.body.dataset.theme = savedTheme;
        }
        
        // Load stats from localStorage if available
        const savedStats = localStorage.getItem('industrialStats');
        if (savedStats) {
            const stats = JSON.parse(savedStats);
            this.activityCount = stats.activityCount || 0;
            this.totalMinutes = stats.totalMinutes || 0;
            
            document.getElementById('activityCount').textContent = this.activityCount;
            document.getElementById('totalMinutes').textContent = this.totalMinutes;
        }
        
        // Auto-save stats periodically
        setInterval(() => {
            this.saveStats();
        }, 10000);
    }

    saveStats() {
        const stats = {
            activityCount: this.activityCount,
            totalMinutes: this.totalMinutes,
            lastUpdated: new Date().toISOString()
        };
        localStorage.setItem('industrialStats', JSON.stringify(stats));
    }
}

// Initialize system when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.boredomSystem = new BoredomDestructionSystem();
    
    // Add conveyor belt background animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes conveyor {
            from { background-position: 0 0; }
            to { background-position: 40px 0; }
        }
        
        .activity-monitor.new-output {
            animation: conveyor 0.5s linear;
        }
    `;
    document.head.appendChild(style);
});