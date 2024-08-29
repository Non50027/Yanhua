import axios from "axios"
import { useRoute } from 'vue-router'
// 取得會員資料
export const getMemberData= async (name)=>{
    return axios.get(`${import.meta.env.VITE_BACKEND}/member/data/?name=${name}`)
    .then(response=> {{
        return response.data
    }})
    .catch(error=> {
        console.log(error.response.data.error)
        return error
    })
};