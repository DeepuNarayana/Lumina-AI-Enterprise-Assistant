import { useState } from "react";
import type { FormEvent } from "react";

import {login} from "../services/authService";

function LoginForm(){

    console.log("LoginForm Rendered");

    const [email, setEmail]=useState("");

    const[password, setPassword]=useState("");

    const handleLogin = async (
        event: FormEvent
    )=> {

        console.log("Login button clicked");

        event.preventDefault();

        //login(email, password);
        const response = await login(
            email,
            password
        );
        console.log("AI Response",response);

    }
    return (

        <form onSubmit={handleLogin}>

            <div>
                <label>Email</label>
                <br/>
                <input

                    type="email"
                    value={email}
                    onChange={(e)=>setEmail(e.target.value)}
                />
            </div>

            <br/>
            <div>
                <label>Password</label>
                <br/>
                <input
                    type="password"
                    value={password}
                    onChange={(e)=>setPassword(e.target.value)}
                />
                <br/>
            </div>
            <br/>
            <button
             type="submit"
             onClick={()=> console.log("Button Clicked")}
             >Login</button>

        </form>
    );
}
export default LoginForm;