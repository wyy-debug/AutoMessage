<template>
  <div class="app-container">
    <!--添加作者信息按钮-->
    <el-row :gutter="10" class="mb8">
      <el-col :span="1.5">
        <el-button type="primary" icon="el-icon-plus" size="mini" @click="handleAdd">新增</el-button>
      </el-col>
    </el-row>
    <!--作者信息列表-->
    <el-table :data="tableData" border style="width: 100%">
      <el-table-column prop="id" label="序号" width="180"></el-table-column>
      <el-table-column prop="name" label="版本名称"></el-table-column>
      <el-table-column label="操作" width="180" align="center">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <!--添加作者信息表单-->
    <el-dialog :title="title" :visible.sync="centerDialogVisible" width="50%" center>
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="版本名称">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="项目id">
          <el-input v-model="form.project_id"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
    <el-button @click="cancel">取 消</el-button>
    <el-button type="primary" @click="save">确 定</el-button>
  </span>
    </el-dialog>
  </div>
</template>

<script>
import {
  createVersionInfo, DeleteVersionInfoById,
  getVersionInfo, UpdateVersionInfoById
} from '@/api/version'

export default {

  data() {
    return {
      title: '添加作者信息',
      tableData: [],
      centerDialogVisible: false,
      form: {
        name: '',
        project_id: 0
      }
    }
  },
  mounted() {
    this.getVersionList()
  },
  methods: {
    handleAdd() {
      this.centerDialogVisible = true
    },
    cancel() {
      this.centerDialogVisible = false
      this.reset()
    },
    reset() {
      this.form = {
        name: '',
        project_id: 0
      }
    },
    handleDelete(index, row) {
      const versionId = row.id
      DeleteVersionInfoById(versionId)
        .then(res => {
          if (res.code === 'success') {
            this.$message.success('删除成功')
            this.getVersionList()
          } else {
            this.$message.error('删除失败')
          }
        })
        .catch(err => {
          console.log(err)
          this.$message.error('删除失败')
        })
    },
    save() {
      console.log(this.title)
      if (this.title === '编辑作者信息') {
        console.log(this.form)
        UpdateVersionInfoById(this.form.id,
          {
            name: this.form.name,
            project_id: this.form.project_id }
        )
          .then(res => {
            if (res.code === 'success') {
              this.$message.success('更新成功')
            } else {
              this.$message.error('更新失败')
            }
          })
          .catch(err => {
            console.log(err)
            this.$message.error('服务端异常，更新失败。')
          })
        this.title = '添加作者信息'
      } else {
        createVersionInfo({
          name: this.form.name,
          project_id: this.form.project_id
        })
          .then(res => {
            if (res.code === 'success') {
              this.$message.success('添加成功')
              this.getVersionList()
            } else {
              this.$message.error('添加失败')
            }
          })
          .catch(err => {
            console.log(err)
            this.$message.error('服务端异常，添加失败。')
          })
      }
      this.centerDialogVisible = false
    },
    getVersionList() {
      getVersionInfo()
        .then(res => {
          console.log(res)
          console.log(res.code)
          if (res.code === 'success') {
            this.tableData = res.versions
          } else {
            this.$message.error('获取信息失败')
          }
        })
        .catch(err => {
          console.log(err)
          this.$message.error('服务端异常，请联系管理员解决。')
        })
    },
    handleEdit(index, row) {
      this.centerDialogVisible = true
      this.title = '编辑作者信息'
      this.form = row
    }
  }
}
</script>

<style scoped>
</style>
