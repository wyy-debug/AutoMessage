<template>
  <div class="app-container">
    <!--添加项目信息按钮-->
    <el-row :gutter="10" class="mb8">
      <el-col :span="1.5">
        <el-button type="primary" icon="el-icon-plus" size="mini" @click="handleAdd">新增</el-button>
      </el-col>
    </el-row>
    <el-collapse v-model="activeName" accordion>
      <el-collapse-item
        v-for="(item,index) in projectData"
        :key = index
        :title = item.project_name
        :name = index >
        <el-row :gutter="10" class="mb8">
          <el-col :span="1.5">
            <el-button type="primary" icon="el-icon-plus" size="mini" @click="handleAddVersion(item.id)">新增版本</el-button>
          </el-col>
        </el-row>
        <el-table :data="item.version" border style="width: 100%">
          <el-table-column prop="name" label="版本"></el-table-column>
          <el-table-column label="操作" width="180" align="center">
            <template slot-scope="scope">
              <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
              <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-collapse-item>
    </el-collapse>

    <!--添加版本信息表单-->
    <el-dialog :title="title" :visible.sync="centerversionDialogVisible" width="50%" center>
      <el-form ref="form" :model="version_from" label-width="80px">
        <el-form-item label="版本名称">
          <el-input v-model="version_from.name"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="cancel">取 消</el-button>
        <el-button type="primary" @click="version_save">确 定</el-button>
      </span>
    </el-dialog>
    <!--添加项目信息表单-->
    <el-dialog :title="title" :visible.sync="centerDialogVisible" width="50%" center>
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="项目名称">
          <el-input v-model="form.project_name"></el-input>
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
  createProjectInfo, DeleteProjectInfoById,
  getProjectInfo, UpdateProjectInfoById
} from '@/api/project'
import { createVersionInfo, getVersionInfoByProjectId } from '@/api/version'
export default {

  data() {
    return {
      activeName: '1',
      title: '添加项目信息',
      projectData: [],
      versionData: [],
      centerDialogVisible: false,
      centerversionDialogVisible: false,
      form: {
        project_name: ''
      },
      version_from: {
        project_id: 0,
        name: ''
      }
    }
  },
  mounted() {
    this.getProjectList()
  },
  methods: {
    handleAdd() {
      this.centerDialogVisible = true
    },
    handleAddVersion: function(param1) {
      this.version_from.project_id = param1
      this.centerversionDialogVisible = true
    },
    cancel() {
      this.centerDialogVisible = false
      this.reset()
    },
    reset() {
      this.form = {
        project_name: ''
      }
    },
    handleDelete(index, row) {
      const projectId = row.id
      DeleteProjectInfoById(projectId)
        .then(res => {
          if (res.code === 'success') {
            this.$message.success('删除成功')
            this.getProjectList()
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
      if (this.title === '编辑项目信息') {
        UpdateProjectInfoById(this.form.id,
          {
            project_name: this.form.project_name }
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
        this.title = '添加项目信息'
      } else {
        createProjectInfo({
          project_name: this.form.project_name
        })
          .then(res => {
            if (res.code === 'success') {
              this.$message.success('添加成功')
              this.getProjectList()
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
    version_save() {
      if (this.title === '编辑项目信息') {
        UpdateProjectInfoById(this.version_from.id,
          {
            name: this.version_from.name,
            project_id: this.version_from.project_id }
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
        this.title = '添加项目信息'
      } else {
        createVersionInfo({
          name: this.version_from.name,
          project_id: this.version_from.project_id
        })
          .then(res => {
            if (res.code === 'success') {
              this.$message.success('添加成功')
              location.reload()
              this.getProjectList()
            } else {
              this.$message.error('添加失败')
            }
          })
          .catch(err => {
            console.log(err)
            this.$message.error('服务端异常，添加失败。')
          })
      }
      this.centerversionDialogVisible = false
    },
    getProjectList() {
      getProjectInfo()
        .then(res => {
          if (res.code === 'success') {
            this.projectData = res.projects
            for (let i = 0; i < this.projectData.length; i++) {
              getVersionInfoByProjectId(this.projectData[i].id).then(res => {
                if (res.code === 'success') {
                  this.projectData[i]['version'] = res.versions
                } else {
                  this.$message.error('获取信息失败')
                }
              }).catch(err => {
                console.log(err)
                this.$message.error('服务端异常，请联系管理员解决。')
              })
            }
            console.log(this.projectData)
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
      this.title = '编辑项目信息'
      this.form = row
    }
  }
}
</script>

<style scoped>
</style>
