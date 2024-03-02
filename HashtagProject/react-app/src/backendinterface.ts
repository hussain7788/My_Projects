import axios, { CancelToken } from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

export function get(fetchUrl: string, queryParams?: any) {
    return axios.get(fetchUrl, {
        params: queryParams
    })
}

