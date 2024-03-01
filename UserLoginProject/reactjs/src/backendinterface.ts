import axios, { CancelToken } from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

export const ADD_CUSTOMER_URL = "http://127.0.0.1:8000/add/customer/"
export const LOGIN_URL = "http://127.0.0.1:8000/login/"
export const LOGOUT_URL = "http://127.0.0.1:8000/logout/"


export function get(fetchUrl: string, queryParams?: any) {
    return axios.get(fetchUrl, {
        params: queryParams
    })
}

export function post(postUrl: string, formData: FormData, queryParams?: any, isFile?: boolean) {
    return axios.post(postUrl, formData, {
        params: queryParams,
    })
}

