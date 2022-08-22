import request from '@/utils/request'

// 添加项目信息
export function createProjectInfo(data) {
  console.log(data)
  return request({
    url: '/project/',
    method: 'post',
    data
  })
}

// 获取所有项目信息
export function getProjectInfo() {
  return request({
    url: '/project/',
    method: 'get'
  })
}

// 通过项目ID获取项目信息
export function getProjectInfoById(id) {
  return request({
    url: '/project/' + id,
    method: 'get'
  })
}

// 更新项目信息（待完善）
export function UpdateProjectInfoById(id, data) {
  return request({
    url: '/project/' + id,
    method: 'patch',
    data
  })
}

// 删除项目信息接口
export function DeleteProjectInfoById(id) {
  return request({
    url: '/project/' + id,
    method: 'delete'
  })
}
