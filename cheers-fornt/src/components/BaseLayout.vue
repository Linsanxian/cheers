<template>
  <div id="base-layout" class="layout">
    <a-layout class="layout">
      <a-layout-header class="header">
        <router-link to="/home">
          <img src="../assets/logo.svg" class="logo">
        </router-link>
      </a-layout-header>
      <a-layout>
        <a-layout-sider>
          <a-menu style="width: 200px"
                  :defaultSelectedKeys="['1']"
                  :openKeys.sync="openKeys"
                  mode="inline"
                  theme="dark"
          >
            <a-menu-item key="index">
              <router-link to="/home">
                <a-icon type="home"/>
                <span>首页</span>
              </router-link>
            </a-menu-item>
            <a-sub-menu key="customers">
            <span slot="title">
              <a-icon type="pie-chart"/>
              客户中心
            </span>

              <a-menu-item key="customer">
                <router-link to="/customer">
                  客户代码
                </router-link>
              </a-menu-item>
              <a-menu-item key="version">
                <router-link to="/versions">
                  版本统计
                </router-link>
              </a-menu-item>
            </a-sub-menu>
          </a-menu>
        </a-layout-sider>
        <a-layout-content>
          <slot></slot>
        </a-layout-content>
      </a-layout>
    </a-layout>
  </div>
</template>

<script>
    export default {
        name: "BaseLayout",
        data() {
            return {
                current: ['mail'],
                openKeys: ['sub1'],
            };
        },
        methods: {
            onclick() {
                this.$router.push({name: 'home'})
            }
        }
    }
</script>

<style>
  .layout {
    height: 100%;
  }

  .logo {
    width: 170px;
  }

  .header {
    padding: 0;
  }
</style>
