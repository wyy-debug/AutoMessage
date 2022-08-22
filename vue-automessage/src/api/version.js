import request from '@/utils/request'

// 添加版本信息
export function createVersionInfo(data) {
  console.log(data)
  return request({
    url: '/version/',
    method: 'post',
    data
  })
}

// 获取所有版本信息
export function getVersionInfo() {
  return request({
    url: '/version/',
    method: 'get'
  })
}

// 通过版本ID获取版本信息
export function getVersionInfoById(id) {
  return request({
    url: '/version/' + id,
    method: 'get'
  })
}

// 通过项目ID获取版本信息
export function getVersionInfoByProjectId(id) {
  return request({
    url: '/version/one/' + id,
    method: 'get'
  })
}

// 更新版本信息（待完善）
export function UpdateVersionInfoById(id, data) {
  return request({
    url: '/version/' + id,
    method: 'patch',
    data
  })
}

// 删除版本信息接口
export function DeleteVersionInfoById(id) {
  return request({
    url: '/version/' + id,
    method: 'delete'
  })
}
