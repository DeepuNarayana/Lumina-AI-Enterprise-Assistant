import { useState } from "react";
import type { FormEvent } from "react";
import {login} from "../services/authService";
import type {ChatMessage} from "../types/chat";


function ChatForm() {

    const [message, setMessage] = useState("");

    //const[response, setResponse] = useState("");

    const [messages, setMessages] = useState<ChatMessage[]>([]);

    const handleSend = async (
        event: FormEvent
    )=> {

        event.preventDefault();

        const result = await login(
            message,
            ""
        );
    const newMessage: ChatMessage = {
        id: Date.now(),
        question: message,
        answer: result.response,
        //time: new Date().toLocaleTimeString(),
        time: new Date().toLocaleString() //this will give both date and
    };
    setMessages([...messages,newMessage]);
    setMessage("");

        //setResponse(result.response);
    };
    return (
        <div>

            <h3>AI Response</h3>

            <div>
                {/*{response}*/}
                {messages.map((chat)=>(
                    <div
                        key={chat.id}
                        style={{
                            border:"1px solid gray",
                            padding:"10px",
                            marginBottom:"10px"
                        }}
                    >
                        <b>You</b>
                        <p>{chat.question}</p>
                        <b>AI</b>
                        <p>{chat.answer}</p>
                        <small>{chat.time}</small>
                    </div>
                ))}
            </div>
            <br/>
            <form onSubmit={handleSend}>
                <label>message</label>
            <br/>
            <input
                type="text"
                value={message}
                onChange={(e)=>
                    setMessage(e.target.value)
                }
                />
                <br/>
                <br/>
                <button type="submit">
                    send
                    </button>
                </form>

        </div>
    );
}
export default ChatForm;
