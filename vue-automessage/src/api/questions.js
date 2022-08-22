// 添加版本信息
import request from '@/utils/request'

export function createQuestionInfo(data) {
  console.log(data)
  return request({
    url: '/questions/',
    method: 'post',
    data
  })
}

export function getQuInfoByVersionId(id) {
  return request({
    url: '/questions/one/?version_id=' + id,
    method: 'get'
  })
}
