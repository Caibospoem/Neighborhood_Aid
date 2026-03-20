<template>
  <div class="home">
    <!-- 装饰元素 -->
    <div class="decoration">🌾</div>
    <div class="decoration">🥕</div>
    <div class="decoration">🍅</div>
    
    <header>
      <div class="logo">
        <div class="logo-icon">🏡</div>
        <div>
          <h1>星露谷邻里互助</h1>
          <p class="subtitle">Stardew Valley Neighborhood Aid</p>
        </div>
      </div>
    </header>
    
    <nav>
      <div class="nav-container">
        <router-link to="/" class="nav-item">
          <span>🏠</span> 首页
        </router-link>
        <a href="#" class="nav-item">
          <span>📋</span> 互助任务
        </a>
        <a href="#" class="nav-item">
          <span>👥</span> 邻里成员
        </a>
        <a href="#" class="nav-item">
          <span>📅</span> 活动日历
        </a>
        <a href="#" class="nav-item">
          <span>💬</span> 社区论坛
        </a>
        <router-link to="/profile" class="nav-item" v-if="isLoggedIn">
          <span>👤</span> 个人中心
        </router-link>
        <router-link to="/auth" class="nav-item" v-else>
          <span>⚙️</span> 登录/注册
        </router-link>
      </div>
    </nav>
    
    <main>
      <section class="welcome-section">
        <div class="welcome-box">
          <h2>欢迎来到星露谷互助社区！</h2>
          <p>在这里，邻里之间互相帮助，共同建设美好的星露谷生活。<br>
          无论是农活帮忙、物品交换，还是社区活动，让我们一起创造温暖的小镇生活。</p>
        </div>
      </section>
      
      <section class="stats-container">
        <div class="stat-box">
          <div class="stat-number">156</div>
          <div class="stat-label">活跃成员</div>
        </div>
        <div class="stat-box">
          <div class="stat-number">892</div>
          <div class="stat-label">完成互助</div>
        </div>
        <div class="stat-box">
          <div class="stat-number">45</div>
          <div class="stat-label">本周活动</div>
        </div>
        <div class="stat-box">
          <div class="stat-number">2341</div>
          <div class="stat-label">互助积分</div>
        </div>
      </section>
      
      <section class="features-grid">
        <div class="feature-card" @click="showFeatureInfo('help')">
          <div class="feature-icon">🤝</div>
          <h3>发布求助</h3>
          <p>需要帮助？发布你的需求，热心的邻居们会伸出援手</p>
        </div>
        <div class="feature-card" @click="showFeatureInfo('offer')">
          <div class="feature-icon">🎁</div>
          <h3>提供帮助</h3>
          <p>有余力？查看邻居们的需求，贡献你的力量</p>
        </div>
        <div class="feature-card" @click="showFeatureInfo('trade')">
          <div class="feature-icon">🔄</div>
          <h3>物品交换</h3>
          <p>多余的农作物、工具？和邻居们进行公平交易</p>
        </div>
        <div class="feature-card" @click="showFeatureInfo('event')">
          <div class="feature-icon">🎉</div>
          <h3>社区活动</h3>
          <p>参与各种有趣的社区活动，增进邻里感情</p>
        </div>
      </section>
      
      <section class="activities-section">
        <h2>最新互助动态</h2>
        <div class="activity-item" v-for="(activity, index) in activities" :key="index" @click="showActivityInfo(activity.title)">
          <div class="activity-title">{{ activity.title }}</div>
          <div class="activity-details">{{ activity.details }}</div>
        </div>
      </section>
    </main>
    
    <footer>
      <p>© 2024 星露谷邻里互助 · 让我们的社区更加温暖</p>
      <p style="margin-top: 10px; font-size: 14px; opacity: 0.8;">
        Inspired by Stardew Valley · Made with ❤️ for our community
      </p>
    </footer>
    
    <!-- 提示框 -->
    <div v-if="showToast" class="toast" @click="closeToast">
      {{ toastMessage }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      isLoggedIn: false,
      activities: [
        {
          title: '李明需要帮忙浇水',
          details: '发布于2小时前 · 需要2人帮忙 · 预计1小时'
        },
        {
          title: '王芳提供新鲜蔬菜交换',
          details: '发布于5小时前 · 可交换南瓜、玉米 · 位置：农场北部'
        },
        {
          title: '社区烧烤聚会本周六举行',
          details: '发布于1天前 · 时间：周六18:00 · 地点：中央广场'
        },
        {
          title: '张伟需要修理工具',
          details: '发布于1天前 · 需要铁匠技能 · 可提供矿石报酬'
        }
      ],
      showToast: false,
      toastMessage: ''
    }
  },
  mounted() {
    this.checkAuthenStatus();
    this.animateElements();
  },
  methods: {
    async checkAuthenStatus() {
      const accessToken = localStorage.getItem('access_token');
      if (accessToken) {
        try {
          // 这里应该调用后端 API 验证 token
          // 暂时模拟登录状态
          this.isLoggedIn = true;
        } catch (error) {
          console.error('检查登录状态失败:', error);
          localStorage.clear();
          this.isLoggedIn = false;
        }
      }
    },
    showFeatureInfo(feature) {
      const messages = {
        help: '发布求助功能即将上线！您可以在这里发布农活、修理、搬运等各种需求。',
        offer: '提供帮助功能即将上线！浏览邻居们的需求，选择您能够帮助的项目。',
        trade: '物品交换功能即将上线！发布您的多余物品，与其他邻居进行公平交易。',
        event: '社区活动功能即将上线！查看和参与各种有趣的社区活动。'
      };
      this.showToastMessage(messages[feature]);
    },
    showActivityInfo(title) {
      this.showToastMessage(`查看详情：${title}`);
    },
    showToastMessage(message) {
      this.toastMessage = message;
      this.showToast = true;
      setTimeout(() => {
        this.showToast = false;
      }, 3000);
    },
    closeToast() {
      this.showToast = false;
    },
    animateElements() {
      const elements = document.querySelectorAll('.feature-card, .stat-box, .activity-item');
      elements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        setTimeout(() => {
          el.style.transition = 'all 0.5s ease-out';
          el.style.opacity = '1';
          el.style.transform = 'translateY(0)';
        }, index * 100);
      });
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Microsoft YaHei', sans-serif;
  background: linear-gradient(to bottom, #87CEEB 0%, #98D98E 50%, #8B7355 100%);
  min-height: 100vh;
  position: relative;
  overflow-x: hidden;
}

/* 像素风格边框 */
.pixel-border {
  border: 4px solid #333;
  box-shadow: 
    0 0 0 4px #fff,
    0 0 0 8px #333,
    0 0 0 12px #fff;
  background: #f4e4c1;
}

/* 头部 */
header {
  background: rgba(255, 255, 255, 0.95);
  padding: 20px;
  text-align: center;
  position: relative;
  z-index: 100;
}

.logo {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
  margin-bottom: 10px;
}

.logo-icon {
  width: 60px;
  height: 60px;
  background: #8B4513;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 30px;
  border: 3px solid #654321;
}

h1 {
  font-family: 'Press Start 2P', cursive;
  font-size: 24px;
  color: #2d5016;
  text-shadow: 2px 2px 0 #fff;
}

.subtitle {
  color: #5a7c47;
  font-size: 16px;
  margin-top: 5px;
}

/* 导航栏 */
nav {
  background: rgba(45, 80, 22, 0.9);
  padding: 15px;
  position: sticky;
  top: 0;
  z-index: 99;
  box-shadow: 0 2px 10px rgba(0,0,0,0.2);
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  gap: 30px;
  flex-wrap: wrap;
}

.nav-item {
  color: #fff;
  text-decoration: none;
  padding: 8px 20px;
  border: 2px solid #fff;
  border-radius: 20px;
  transition: all 0.3s;
  font-weight: bold;
  display: flex;
  align-items: center;
  gap: 8px;
}

.nav-item:hover {
  background: #fff;
  color: #2d5016;
  transform: translateY(-2px);
}

/* 主要内容区 */
main {
  max-width: 1200px;
  margin: 30px auto;
  padding: 0 20px;
}

/* 欢迎区域 */
.welcome-section {
  text-align: center;
  margin-bottom: 40px;
  animation: fadeIn 1s ease-out;
}

.welcome-box {
  display: inline-block;
  padding: 30px 50px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

.welcome-box h2 {
  color: #2d5016;
  font-size: 28px;
  margin-bottom: 15px;
}

.welcome-box p {
  color: #5a7c47;
  font-size: 18px;
  line-height: 1.6;
}

/* 功能卡片 */
.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-bottom: 40px;
}

.feature-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 15px;
  padding: 25px;
  text-align: center;
  transition: all 0.3s;
  cursor: pointer;
  border: 3px solid transparent;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  border-color: #8B4513;
}

.feature-icon {
  font-size: 50px;
  margin-bottom: 15px;
}

.feature-card h3 {
  color: #2d5016;
  font-size: 20px;
  margin-bottom: 10px;
}

.feature-card p {
  color: #666;
  line-height: 1.5;
}

/* 活动列表 */
.activities-section {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 15px;
  padding: 30px;
  margin-bottom: 40px;
}

.activities-section h2 {
  color: #2d5016;
  font-size: 24px;
  margin-bottom: 20px;
  text-align: center;
}

.activity-item {
  background: #f9f5eb;
  border-left: 5px solid #8B4513;
  padding: 15px 20px;
  margin-bottom: 15px;
  border-radius: 0 10px 10px 0;
  transition: all 0.3s;
}

.activity-item:hover {
  transform: translateX(5px);
  box-shadow: -5px 0 15px rgba(139, 69, 19, 0.2);
  cursor: pointer;
}

.activity-title {
  font-weight: bold;
  color: #2d5016;
  margin-bottom: 5px;
}

.activity-details {
  color: #666;
  font-size: 14px;
}

/* 统计数据 */
.stats-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 40px;
}

.stat-box {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 15px;
  padding: 25px;
  text-align: center;
  border: 3px solid #8B4513;
}

.stat-number {
  font-size: 36px;
  font-weight: bold;
  color: #2d5016;
  margin-bottom: 5px;
}

.stat-label {
  color: #5a7c47;
  font-size: 16px;
}

/* 页脚 */
footer {
  background: rgba(45, 80, 22, 0.9);
  color: #fff;
  text-align: center;
  padding: 30px;
  margin-top: 50px;
}

/* 动画 */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 响应式设计 */
@media (max-width: 768px) {
  h1 {
    font-size: 18px;
  }
  
  .nav-container {
    gap: 15px;
  }
  
  .nav-item {
    font-size: 14px;
    padding: 6px 15px;
  }
  
  .welcome-box {
    padding: 20px 30px;
  }
  
  .welcome-box h2 {
    font-size: 22px;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
  }
}

/* 装饰元素 */
.decoration {
  position: fixed;
  font-size: 30px;
  animation: float 6s ease-in-out infinite;
  z-index: 1;
  opacity: 0.3;
}

.decoration:nth-child(1) {
  top: 20%;
  left: 5%;
  animation-delay: 0s;
}

.decoration:nth-child(2) {
  top: 60%;
  right: 5%;
  animation-delay: 2s;
}

.decoration:nth-child(3) {
  bottom: 20%;
  left: 10%;
  animation-delay: 4s;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
}

/* 提示框 */
.toast {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: rgba(45, 80, 22, 0.95);
  color: white;
  padding: 20px 30px;
  border-radius: 10px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.3);
  z-index: 1000;
  max-width: 400px;
  text-align: center;
  animation: fadeIn 0.3s ease-out;
  cursor: pointer;
}
</style>