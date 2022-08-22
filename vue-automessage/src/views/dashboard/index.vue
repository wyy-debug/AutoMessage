<template>
  <div class="dashboard-container">

    <el-select v-model="project_name" clearable filterable="true" placeholder="请选择" @change="getVersionList">
      <el-option
        v-for="item in projects"
        :key="item.id"
        :value="item.project_name">
      </el-option>
    </el-select>
    <el-select v-model="name" clearable filterable="true" placeholder="请选择" style="visibility: visible">
      <el-option
        v-for="item in versions"
        :key="item.name"
        :value="item.name"
      >
      </el-option>
    </el-select>
    <el-button type="primary" size="medium" @click="getQuestionList">查询</el-button>

    <el-row :gutter="10" class="row-top" v-if="questionVisible">
      <el-col :span="6">
        <div class="grid-content-text">功能</div>
        <div>
          <div class="grid-content bg-purple" @dblclick="handleAdd">
            <ComponentName v-for="(item,index) in function_questions" ref="ComponentName" :key="index" :id="item.id" :bug_message="item.question_msg" :owner="item.question_author"></ComponentName>
          </div>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content-text">性能</div>
        <div>
          <div class="grid-content bg-purple" @dblclick="handleAdd">
            <ComponentName v-for="(item,index) in performance_questions" ref="ComponentName" :key="index" :id="item.id" :bug_message="item.question_msg" :owner="item.question_author"></ComponentName>
          </div>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content-text">兼容</div>
        <div>
          <div class="grid-content bg-purple" @dblclick="handleAdd">
            <ComponentName v-for="(item,index) in compatible_questions" ref="ComponentName" :key="index" :id="item.id" :bug_message="item.question_msg" :owner="item.question_author"></ComponentName>
          </div>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content-text">异常</div>
        <div>
          <div class="grid-content bg-purple" @dblclick="handleAdd">
            <ComponentName v-for="(item,index) in abnormal_questions" ref="ComponentName" :key="index" :id="item.id" :bug_message="item.question_msg" :owner="item.question_author"></ComponentName>
          </div>
        </div>
      </el-col>
    </el-row>
    <el-dialog title="新建bug" :visible.sync="centerDialogVisible" :close-on-click-modal="false">
      <div>风险等级 高中低</div>
      <div>问题描述</div>
      <MyEditor></MyEditor>
      <span slot="footer" class="dialog-footer">
        <el-button @click="cancel">取 消</el-button>
        <el-button type="primary" @click="save">确 定</el-button>
      </span>
    </el-dialog>
    <el-drawer
      title="新建bug"
      :visible.sync="drawer"
      :with-header="false">
      <span>新建bug</span>
    </el-drawer>
  </div>
</template>

<script>
import ComponentName from '@//views/questionborad/main'
import MyEditor from '@/views/questionborad/newquestion'
import { mapGetters } from 'vuex'
import { getProjectInfo } from '@/api/project'
import { getVersionInfoByProjectId } from '@/api/version'
import { createQuestionInfo, getQuInfoByVersionId } from '@/api/questions'

// import { getBpInfoByVersionId } from '@/api/bp'

export default {
  components: { MyEditor, ComponentName },
  data() {
    return {
      drawer: false,
      questionVisible: false,
      bp: [{
        name: '',
        id: 0
      }],
      function_questions: [],
      performance_questions: [],
      compatible_questions: [],
      abnormal_questions: [],
      centerDialogVisible: false,
      count: 0,
      projects: [{
        id: 0,
        project_name: ''
      }],
      project_name: '',
      versions: [{
        id: 0,
        name: ''
      }],
      versions_id: 0,
      name: '',
      form: {
        msg: '',
        bulletin_board_id: 0
      }
    }
  },
  methods: {
    setdrawer(event) {
      const el1 = event.currentTarget
      const el2 = event.target
      if (el1 === el2) {
        this.drawer = true
      }
    },
    getQuestionList() {
      if (this.name === '') {
        return
      } else {
        for (var i = 0; i < this.versions.length; i++) {
          if (this.versions[i].name === this.name) {
            this.versions_id = this.versions[i].id
            getQuInfoByVersionId(this.versions[i].id).then(res => {
              if (res.code === 'success') {
                this.function_questions = []
                this.performance_questions = []
                this.compatible_questions = []
                this.abnormal_questions = []
                for (var j = 0; j < res.question.length; j++) {
                  switch (res.question[j].question_type) {
                    case '功能':
                      this.function_questions.push(res.question[j])
                      break
                    case '性能':
                      this.performance_questions.push(res.question[j])
                      break
                    case '兼容':
                      this.compatible_questions.push(res.question[j])
                      break
                    case '异常':
                      this.abnormal_questions.push(res.question[j])
                      break
                    case '初始':
                      break
                  }
                }
                this.questionVisible = true
              } else {
                this.$message.error('获取信息失败')
                this.questionVisible = false
              }
            })
              .catch(err => {
                console.log(err)
                this.$message.error('服务端异常，12312。')
                this.questionVisible = false
              })
          }
        }
      }
    },
    handleAdd() {
      this.centerDialogVisible = true
      for (var i = 0; i < this.versions.length; i++) {
        if (this.versions[i].name === this.name) {
          console.log(this.versions[i].id)
          break
        }
      }
      // getBpInfoByVersionId(this.versions[i].id, param1).then(res => {
      //   if (res.code === 'success') {
      //     this.bp = res.bp
      //   } else {
      //     this.$message.error('获取信息失败')
      //   }
      // })
      //   .catch(err => {
      //     console.log(err)
      //     this.$message.error('服务端异常，请联系管理员解决。')
      //   })
    },
    cancel() {
      this.centerDialogVisible = false
      this.reset()
    },
    save() {
      createQuestionInfo({
        msg: this.form.msg,
        bulletin_board_id: this.bp[0].id
      })
        .then(res => {
          if (res.code === 'success') {
            this.$message.success('添加成功')
            this.getQuestionList()
          } else {
            this.$message.error('添加失败')
          }
        })
        .catch(err => {
          console.log(err)
          this.$message.error('服务端异常，添加失败。')
        })
      this.centerDialogVisible = false
    },
    getProjectList() {
      getProjectInfo()
        .then(res => {
          if (res.code === 'success') {
            console.log(res.projects)
            this.projects = res.projects
          } else {
            this.$message.error('获取信息失败')
          }
        })
        .catch(err => {
          console.log(err)
          this.$message.error('服务端异常，请联系管理员解决。')
        })
    },
    getVersionList() {
      for (var i = 0; i < this.projects.length; i++) {
        this.name = ''
        if (this.projects[i].project_name === this.project_name) {
          console.log(this.projects[i].id)
          getVersionInfoByProjectId(this.projects[i].id).then(res => {
            if (res.code === 'success') {
              console.log(res.versions)
              this.versions = res.versions
            } else {
              this.$message.error('获取信息失败')
            }
          }).catch(err => {
            console.log(err)
            this.$message.error('服务端异常，请联系管理员解决。')
          })
        }
      }
    }
  },
  mounted() {
    this.getProjectList()
  },
  computed: {
    ComponentName,
    ...mapGetters([
      'name'
    ])
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
.el-dropdown-link {
  cursor: pointer;
  color: #409EFF;
}
.el-icon-arrow-down {
  font-size: 12px;
}
.demonstration {
  display: block;
  color: #f2f3f6;
  font-size: 14px;
  margin-bottom: 20px;
}.el-row {
   margin-bottom: 20px;
   &:last-child {
     margin-bottom: 0;
   }
 }
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #f2f3f6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 1800px;
  margin-top: 10px;
}
.grid-content-text {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: small;
  font-weight: bold;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.row-top{
  margin-top: 10px;
}
</style>
