<template>
  <div class="dashboard-container">
    <el-tag>当前选择卡</el-tag>
    <el-tag type="success">设备是否繁忙</el-tag>
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
        prop="date"
        label="设备"
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="分区"
        width="180">
      </el-table-column>
      <el-table-column
        prop="address"
        label="分号">
      </el-table-column>
      <el-table-column
        prop="phone_number"
        label="手机号码">
      </el-table-column>
      <el-table-column
        prop="message"
        label="信息">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>

import { ChangeDevices, getDevicesInfo } from '@/api/devices'

export default {
  mobile: '123',
  partition: '123',
  number: '123',
  components: { },
  data() {
    return {
      tableData: [{
        date: '荣耀 V10',
        name: '分区1',
        address: 'SIM1',
        phone_number: '13333333333',
        message: 'test11111'
      }, {
        date: '荣耀 V10',
        name: '分区1',
        address: 'SIM1',
        phone_number: '13333333333',
        message: 'test11111'
      }, {
        date: '荣耀 V10',
        name: '分区1',
        address: 'SIM1',
        phone_number: '13333333333',
        message: 'test11111'
      }, {
        date: '荣耀 V10',
        name: '分区1',
        address: 'SIM1',
        phone_number: '13333333333',
        message: 'test11111'
      }],
      value: [],
      options: []
    }
  },
  methods: {
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
      ChangeDevices(devices_json)
    }
  },
  mounted() {
    this.getDevicesList()
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
