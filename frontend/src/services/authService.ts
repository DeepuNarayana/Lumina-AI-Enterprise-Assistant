import axios from "axios";
import api from "../api/api";


export async function login(

    email: string,
    password: string

){
    console.log("Inside AuthService");
    try {
        const response = await api.post(
            "/ai/chat",
            {
                message: `Login attempt by ${email}`
            }
        );
        return response.data
        //console.log(response.data);
        console.log(password);
    }catch(error){
        if (axios.isAxiosError(error)){
            console.log("Axios Error");
            console.log(error.message);
            console.log(error.response)
        }
        else{
                console.log(error);
        }
    }
}