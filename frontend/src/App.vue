<template>
  <router-view />
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
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
</style>