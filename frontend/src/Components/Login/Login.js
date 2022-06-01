import React, { useState } from 'react'
import { Form, Button, Container, Row } from 'react-bootstrap'
import './Login.css'
import { useForm } from 'react-hook-form'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import jwt_decode from "jwt-decode";

export const Login = () => {

    const { register, handleSubmit, setError, formState: { errors } } = useForm();
    const navigate = useNavigate()
    const [Err, setErs] = useState("")
    const handleSubmitLogin = async (data) => {
        const datas = {
            username: data.username,
            password: data.password
        }

        try {
            const { data } = await axios.post('http://127.0.0.1:8000/api/login/', datas)
            localStorage.setItem("userAccessToken", data.access)
            console.log(data);
            localStorage.setItem("userRefreshToken", data.refresh)
            const userAccessToken = localStorage.getItem("userAccessToken")
            console.log(userAccessToken);

            if (userAccessToken) {
                const decode = jwt_decode(userAccessToken)
                if (decode.is_customer) {
                    console.log(decode.is_customer);
                    navigate("/")
                }
                else {
                    navigate("login")
                }
            }

        }
        catch (Err) {
            setErs(Err.response.data.username)
        }
    }
    return (
        <Container className='main_container'>
            <Row>
                <div className='login_form'>
                    <h2 className='heading'>Login</h2>
                    <Form onClick={handleSubmit(handleSubmitLogin)}>
                        <Form.Group className="mb-3" controlId="formBasicEmail">
                            <Form.Label>Username</Form.Label>
                            <Form.Control
                                type="text"
                                {...register("username", { required: "username is required" })}
                                placeholder="Username" />
                            {errors.username && <p style={{ color: 'red', fontSize: 'smaller' }}>{errors.username.message}</p>}
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="formBasicPassword">
                            <Form.Label>Password</Form.Label>
                            <Form.Control
                                type="password"
                                {...register("password", { required: "password is required" })}
                                placeholder="Password" />
                            {errors.password && <p style={{ color: 'red', fontSize: 'smaller' }}>{errors.password.message}</p>}
                        </Form.Group>

                        <button type="submit" className='login_button' >
                            Submit
                        </button>
                    </Form>
                </div>
            </Row>
        </Container>
    )
}
