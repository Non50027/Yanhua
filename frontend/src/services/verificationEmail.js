import axios from "axios"
// 寄送驗證信件
export const verificationEmail= (name)=>{
    return axios.post(`${import.meta.env.VITE_BACKEND}/member/verification/${name}`)
    .then(response => {
        alert(response.data.message);
    })
    .catch(error => {
        console.log()
        console.log('send-Email error', error.response.data.error)
    });
};
