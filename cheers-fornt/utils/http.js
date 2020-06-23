import axios from 'axios'

if (process.env.NODE_ENV === 'development') {
  axios.defaults.baseURL = 'http://localhost:8000'
} else if (process.env.NODE_ENV === 'production') {
  axios.defaults.baseURL = process.env.API_SERVER_URL
}

axios.defaults.timeout = 10000


axios.interceptors.response.use(response => {
  if (response.status === 200) {
    if (response.data.code === 500) {
    } else if (response.data.code === 510) {
    } else {
      return Promise.resolve(response)
    }
  } else {
    return Promise.reject(response)
  }
}, error => {
  if (error.response.status) {
    return Promise.reject(error.response)
  }
})

export function httpGet(
  {
    url,
    params = {}
  }) {
  return new Promise((resolve, reject) => {
    axios.get(url, {
      params
    }).then((res) => {
      resolve(res.data)
    }).catch(err => {
      reject(err)
    })
  })
}

// post请求
export function httpPost(
  {
    url,
    data = {},
    params = {}
  }) {
  return new Promise((resolve, reject) => {
    axios({
      url,
      method: 'post',
      transformRequest: [function (data) {
        let ret = ''
        for (let it in data) {
          ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
        }
        return ret
      }],
      data,
      params

    }).then(res => {
      resolve(res.data)
    })
  })
}
