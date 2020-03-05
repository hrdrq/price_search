// import axios from 'axios'

let _axios = Object
_axios.get = path => {
  if(path === '/api/rate') {
    return new Promise((resolve, reject) => { // eslint-disable-line no-unused-vars
      setTimeout(() => {
        resolve({
          data: {status: 'success', rate: 3.62},
          status: 200,
          statusText: "OK"
        })
      }, Math.floor(Math.random() * Math.floor(3000)))
    })
  }
  else {
    const platform = /\/api\/search\/(.+?)(\?|$)/.exec(path)[1]
    return new Promise((resolve, reject) => { // eslint-disable-line no-unused-vars
      setTimeout(() => {
        resolve({
          data: require('../res_mock/' + platform + '.json'),
          status: 200,
          statusText: "OK"
        })
      }, Math.floor(Math.random() * Math.floor(3000)))
    })
  }
}

export default _axios
