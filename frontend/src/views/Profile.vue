<template>
  <div class="profile">
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
        <router-link to="/profile" class="nav-item">
          <span>👤</span> 个人中心
        </router-link>
        <router-link to="/auth" class="nav-item" @click="logout">
          <span>🚪</span> 退出登录
        </router-link>
      </div>
    </nav>
    
    <main>
      <section class="profile-section">
        <div class="profile-card">
          <div class="profile-header">
            <div class="avatar">
              <img src="../assets/hero.png" alt="用户头像" />
            </div>
            <div class="user-info">
              <h2>{{ user.name }}</h2>
              <p class="user-role">{{ user.role }}</p>
              <p class="user-location">{{ user.location }}</p>
            </div>
          </div>
          
          <div class="profile-stats">
            <div class="stat-item">
              <div class="stat-value">{{ user.helpCount }}</div>
              <div class="stat-label">帮助次数</div>
            </div>
            <div class="stat-item">
              <div class="stat-value">{{ user.helpedCount }}</div>
              <div class="stat-label">被帮助次数</div>
            </div>
            <div class="stat-item">
              <div class="stat-value">{{ user.points }}</div>
              <div class="stat-label">互助积分</div>
            </div>
            <div class="stat-item">
              <div class="stat-value">{{ user.level }}</div>
              <div class="stat-label">社区等级</div>
            </div>
          </div>
          
          <div class="profile-tabs">
            <button class="tab-button" :class="{ active: activeTab === 'tasks' }" @click="activeTab = 'tasks'">
              我的任务
            </button>
            <button class="tab-button" :class="{ active: activeTab === 'history' }" @click="activeTab = 'history'">
              历史记录
            </button>
            <button class="tab-button" :class="{ active: activeTab === 'settings' }" @click="activeTab = 'settings'">
              个人设置
            </button>
          </div>
          
          <div class="tab-content">
            <div v-if="activeTab === 'tasks'" class="tasks-tab">
              <h3>我的任务</h3>
              <div class="task-item" v-for="(task, index) in tasks" :key="index">
                <div class="task-title">{{ task.title }}</div>
                <div class="task-status" :class="task.status">{{ task.statusText }}</div>
                <div class="task-details">{{ task.details }}</div>
              </div>
            </div>
            
            <div v-if="activeTab === 'history'" class="history-tab">
              <h3>历史记录</h3>
              <div class="history-item" v-for="(history, index) in history" :key="index">
                <div class="history-title">{{ history.title }}</div>
                <div class="history-date">{{ history.date }}</div>
                <div class="history-details">{{ history.details }}</div>
              </div>
            </div>
            
            <div v-if="activeTab === 'settings'" class="settings-tab">
              <h3>个人设置</h3>
              <form class="settings-form">
                <div class="form-group">
                  <label>用户名</label>
                  <input type="text" v-model="user.name" />
                </div>
                <div class="form-group">
                  <label>邮箱</label>
                  <input type="email" v-model="user.email" />
                </div>
                <div class="form-group">
                  <label>位置</label>
                  <input type="text" v-model="user.location" />
                </div>
                <div class="form-group">
                  <label>年龄</label>
                  <input type="number" v-model="user.age" />
                </div>
                <button type="button" class="save-button" @click="saveSettings">保存设置</button>
              </form>
            </div>
          </div>
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
  name: 'Profile',
  data() {
    return {
      user: {
        name: '星露谷居民',
        role: '普通成员',
        location: '星露谷农场',
        age: 25,
        email: 'farmer@stardewvalley.com',
        helpCount: 12,
        helpedCount: 8,
        points: 156,
        level: 3
      },
      activeTab: 'tasks',
      tasks: [
        {
          title: '帮忙收割小麦',
          status: 'completed',
          statusText: '已完成',
          details: '帮助邻居收割小麦，获得 20 积分'
        },
        {
          title: '寻找丢失的工具',
          status: 'pending',
          statusText: '进行中',
          details: '帮助寻找邻居丢失的工具'
        },
        {
          title: '分享新鲜蔬菜',
          status: 'completed',
          statusText: '已完成',
          details: '分享新鲜蔬菜给邻居，获得 15 积分'
        }
      ],
      history: [
        {
          title: '帮助收割小麦',
          date: '2024-06-01',
          details: '帮助邻居收割小麦，获得 20 积分'
        },
        {
          title: '分享新鲜蔬菜',
          date: '2024-05-28',
          details: '分享新鲜蔬菜给邻居，获得 15 积分'
        },
        {
          title: '参加社区聚会',
          date: '2024-05-20',
          details: '参加社区烧烤聚会，获得 10 积分'
        }
      ],
      showToast: false,
      toastMessage: ''
    }
  },
  methods: {
    logout() {
      localStorage.clear();
      this.$router.push('/auth');
    },
    saveSettings() {
      this.showToastMessage('设置保存成功！');
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

/* 个人资料区域 */
.profile-section {
  display: flex;
  justify-content: center;
  margin-bottom: 40px;
}

.profile-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 15px;
  padding: 30px;
  width: 100%;
  max-width: 800px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

.profile-header {
  display: flex;
  align-items: center;
  gap: 30px;
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 2px solid #8B4513;
}

.avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  overflow: hidden;
  border: 4px solid #8B4513;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.user-info h2 {
  color: #2d5016;
  font-size: 24px;
  margin-bottom: 5px;
}

.user-role {
  color: #8B4513;
  font-weight: bold;
  margin-bottom: 5px;
}

.user-location {
  color: #5a7c47;
  font-size: 16px;
}

/* 统计数据 */
.profile-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
  padding: 20px;
  background: #f9f5eb;
  border-radius: 10px;
}

.stat-item {
  text-align: center;
}

.stat-value {
  font-size: 24px;
  font-weight: bold;
  color: #2d5016;
  margin-bottom: 5px;
}

.stat-label {
  color: #5a7c47;
  font-size: 14px;
}

/* 标签页 */
.profile-tabs {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
  border-bottom: 2px solid #8B4513;
  padding-bottom: 10px;
}

.tab-button {
  padding: 10px 20px;
  border: none;
  background: transparent;
  color: #5a7c47;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s;
  border-radius: 5px;
}

.tab-button:hover {
  background: #f9f5eb;
}

.tab-button.active {
  background: #8B4513;
  color: #fff;
}

/* 标签内容 */
.tab-content {
  min-height: 300px;
}

.tasks-tab h3,
.history-tab h3,
.settings-tab h3 {
  color: #2d5016;
  font-size: 20px;
  margin-bottom: 20px;
}

/* 任务项 */
.task-item {
  background: #f9f5eb;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 10px;
  border-left: 5px solid #8B4513;
}

.task-title {
  font-weight: bold;
  color: #2d5016;
  margin-bottom: 5px;
}

.task-status {
  display: inline-block;
  padding: 3px 10px;
  border-radius: 15px;
  font-size: 12px;
  font-weight: bold;
  margin-bottom: 5px;
}

.task-status.completed {
  background: #98D98E;
  color: #2d5016;
}

.task-status.pending {
  background: #FFD700;
  color: #8B4513;
}

.task-details {
  color: #666;
  font-size: 14px;
}

/* 历史记录项 */
.history-item {
  background: #f9f5eb;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 10px;
  border-left: 5px solid #5a7c47;
}

.history-title {
  font-weight: bold;
  color: #2d5016;
  margin-bottom: 5px;
}

.history-date {
  color: #8B4513;
  font-size: 12px;
  margin-bottom: 5px;
}

.history-details {
  color: #666;
  font-size: 14px;
}

/* 设置表单 */
.settings-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.form-group label {
  color: #2d5016;
  font-weight: bold;
  font-size: 14px;
}

.form-group input {
  padding: 10px;
  border: 2px solid #8B4513;
  border-radius: 5px;
  font-size: 16px;
}

.save-button {
  padding: 12px 24px;
  background: #8B4513;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s;
  align-self: flex-start;
}

.save-button:hover {
  background: #654321;
  transform: translateY(-2px);
}

/* 页脚 */
footer {
  background: rgba(45, 80, 22, 0.9);
  color: #fff;
  text-align: center;
  padding: 30px;
  margin-top: 50px;
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

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translate(-50%, -50%) translateY(20px);
  }
  to {
    opacity: 1;
    transform: translate(-50%, -50%) translateY(0);
  }
}

/* 响应式设计 */
@media (max-width: 768px) {
  .profile-header {
    flex-direction: column;
    text-align: center;
    gap: 20px;
  }
  
  .profile-stats {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .profile-tabs {
    flex-wrap: wrap;
  }
  
  .tab-button {
    flex: 1;
    min-width: 100px;
  }
}
</style>