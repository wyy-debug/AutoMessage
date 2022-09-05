<template>
  <div class="dashboard-container">
    <el-tag :data="phone_now">当前选择卡 {{phone_now}}</el-tag>
    <el-tag type="success" :data="phone_state">设备是否繁忙 {{phone_state}}</el-tag>
    <div class="block">
      <span class="demonstration">选择切卡</span>
      <el-cascader
        v-model="value"
        :options="options"
        :show-all-levels="false"></el-cascader>
      <el-button @click="save">点击切卡</el-button>
    </div>
    <div> 短信列表 </div>
    <el-table
      :data="tableData"
      stripe
      style="width: 100%">
      <el-table-column
        prop="recv_from_number"
        label="号码"
        width="180">
      </el-table-column>
      <el-table-column
        prop="message_text"
        label="信息"
        width="900">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>

import { ChangeDevices, getDeviceInfo, getDevicesInfo, getMessagesInfo } from '@/api/devices'

export default {
  mobile: '123',
  partition: '123',
  number: '123',
  components: { },
  data() {
    return {
      phone_state: '忙碌',
      phone_now: '无',
      tableData: [],
      value: [],
      options: []
    }
  },
  created() {
    setInterval(() => {
      this.getMessageList()
      this.getDevicesState()
    }, 1000 * 5)
  },
  methods: {
    getMessageList() {
      getMessagesInfo()
        .then(res => {
          if (res.code === 'success') {
            this.tableData = res.messages
          } else {
            this.$message.error('获取信息失败')
          }
        })
        .catch(err => {
          console.log(err)
          this.$message.error('服务端异常，请联系管理员解决。')
        })
    },
    getDevicesState() {
      getDeviceInfo()
        .then(res => {
          if (res.code === 'success') {
            this.phone_state = res.data['phone_state']
            this.phone_now = res.data['phone_now']
          } else {
            this.$message.error('获取信息失败')
          }
        })
        .catch(err => {
          console.log(err)
          this.$message.error('服务端异常，请联系管理员解决。')
        })

    },
    getDevicesList() {
      getDevicesInfo()
        .then(res => {
          if (res.code === 'success') {
            this.options = res.options
          } else {
            this.$message.error('获取信息失败')
          }
        })
        .catch(err => {
          console.log(err)
          this.$message.error('服务端异常，请联系管理员解决。')
        })
    },
    save() {
      var devices_json = { devices_name: this.value[0], partition: this.value[1], phone_type: this.value[2], phone_number: this.value[3] }
      ChangeDevices(devices_json).then(res => {
        if (res.code === 'success') {
          this.phone_state = res.data['phone_state']
          this.phone_now = res.data['phone_now']
        } else {
          this.$message.error('切卡失败')
        }
      })
        .catch(err => {
          console.log(err)
          this.$message.error('切卡失败')
        })
    }
  },
  mounted() {
    this.getDevicesList()
    this.getMessageList()
    this.getDevicesState()
  },
  computed: {
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
