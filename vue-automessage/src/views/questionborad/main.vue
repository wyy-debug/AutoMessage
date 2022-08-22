
<template>
  <div class="componentName question_form">
    <el-card class="box-card" >
      <el-link class="text item" type="primary">
        {{ id }}
      </el-link>
      <div class="text item" style="white-space: pre-wrap;">
        {{ bug_message }}
      </div>
      <el-button @click="drawer_t = true">
        点我打开
      </el-button>
      <div class="text item">
        {{ owner }}
      </div>
      <el-drawer
        title="我是标题"
        :visible.sync="drawer_t"
        :with-header="false">
        <span>
          <el-link type="primary">默认链接</el-link>
          <el-collapse v-model="activeNames">
            <el-collapse-item title="问题详情" name="1">
              <div>{{ bug_message }}</div>
            </el-collapse-item>
            <el-collapse-item title="用户" name="2">
              <div>{{ owner }}</div>
            </el-collapse-item>
          </el-collapse>
        </span>
      </el-drawer>
    </el-card>
  </div>
</template>

<script>

export default {
  name: 'ComponentName',
  components: {},
  props: {
    id: {},
    // eslint-disable-next-line vue/require-prop-type-constructor
    bug_message: '',
    // eslint-disable-next-line vue/require-prop-type-constructor
    owner: '',
    // eslint-disable-next-line vue/require-prop-type-constructor
    testdrawer: false
  },
  data() {
    return {
      activeNames: ['1', '2'],
      drawer_t: false
    }
  },
  computed: {},
  methods: {},
  beforeCreate() {},
  created() {},
  beforeMount() {},
  mounted() {},
  beforeUpdate() {},
  updated() {},
  beforeDestroy() {},
  destroyed() {},
  watch: {}

}
</script>

<style lang="scss" scoped>
.componentName{}
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both
}

.box-card {
  width: 450px;
  margin-top: 10px;
  margin-right: 10px;
  margin-left: 10px;
}
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.question_form {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
