// 获取所有项目信息
import request from '@/utils/request'

export function getDevicesInfo() {
  return request({
    url: '/device/',
    method: 'get'
  })
}
export function ChangeDevices(data) {
  return request({
    url: '/device/changedevices/',
    method: 'post',
    data
  })
}

export function getMessagesInfo() {
  return request({
    url: '/message/',
    method: 'get'
  })
}

export function getDeviceInfo() {
  return request({
    url: '/device/devicesstate/',
    method: 'get'
  })
}
