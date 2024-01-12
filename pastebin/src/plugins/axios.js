import axios from "axios";
import { getAuthHeader } from "@/utils";

// Full config:  https://github.com/axios/axios#request-config
// axios.defaults.baseURL = process.env.baseURL || process.env.apiUrl || '';
// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

let config = {
  // using flask server
  baseURL: process.env.VUE_APP_SERVER_URL,
  timeout: 60 * 1000,
  withCredentials: true,
};

const _axios = axios.create(config);

_axios.interceptors.request.use(
  function(config) {
    // Do something before request is sent
    return config;
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

// Add a response interceptor
_axios.interceptors.response.use(
  function(response) {
    // Do something with response data
    return response;
  },
  function(error) {
    // Do something with response error
    return Promise.reject(error);
  }
);

export function setupAxios(app) {
  axios.defaults.baseURL = process.env.VUE_APP_SERVER_URL;
  app.config.globalProperties.$axios = _axios;
  // set token in local storage to null
  axios.defaults.headers.common['Authorization'] = getAuthHeader();
}