import axios, { CancelToken } from "axios";


axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

export function getCancelToken() {
    return axios.CancelToken.source()
}

export function get(fetchUrl: string, cancelToken?: CancelToken, queryParams?: any) {
    return axios.get(fetchUrl, {
        cancelToken: cancelToken,
        params: queryParams
    })
}

export function del(postUrl: string, queryParams?: any) {
    return axios.delete(postUrl, {
        params: queryParams
    })
}

export function post(postUrl: string, formData: FormData, cancelToken?: CancelToken, queryParams?: any, isFile?: boolean) {
    if (isFile != undefined && isFile) {
        return axios.post(postUrl, formData, {
            cancelToken: cancelToken,
            params: queryParams,
            headers: {
                "content-type": "multipart/form-data"
            }
        })
    }
    return axios.post(postUrl, formData, {
        cancelToken: cancelToken,
        params: queryParams,
    })
}