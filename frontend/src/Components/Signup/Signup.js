import React, { useState } from 'react'
import { Form, Button, Container, Row, Col } from 'react-bootstrap'
import { useForm } from 'react-hook-form'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import './Signup.css'

export const Signup = () => {

    const navigate = useNavigate()
    const { register, handleSubmit, setError, formState: { errors } } = useForm();

    const [Err, setErr] = useState("")
    const handleSubmitSignup = async (data) => {
        console.log(data);
        const datas = {
            name: data.name,
            username: data.username,
            email: data.email,
            password: data.password,
            mobile: data.mobile,
            age: data.age,
            weight: data.weight,
            height: data.height,

        }

        try {

            const response = await axios.post('http://127.0.0.1:8000/api/signup/', datas)
            console.log(datas);
            console.log(response);
            navigate("/")
        }
        catch (Err) {

            setErr(Err.response.data.username)

        }
    }


    return (

        <Container className='main_container'>
            <Row>
                <div className='form-container'>
                    <h2 className='heading'>Register</h2>


                    <Form onClick={handleSubmit(handleSubmitSignup)}>
                        <Row >
                            <Col>
                                <Form.Group className="mb-3" controlId="formBasicName">
                                    <Form.Label>Name</Form.Label>
                                    <Form.Control
                                        type="text"
                                        {...register("name", { required: "name is required", minLength: { value: 4, message: "should contain minimum 4 characters" } })}
                                        placeholder="Name" />

                                    {errors.name && <p style={{ color: 'red', fontSize: 'smaller' }}>{errors.name.message}</p>}
                                </Form.Group>

                                <Form.Group className="mb-3" controlId="formBasicUsername">
                                    <Form.Label>Username</Form.Label>
                                    <Form.Control
                                        type="text"
                                        {...register("username", { required: "username is required", minLength: { value: 4, message: "should contain minimum 4 characters" } })}
                                        placeholder="Username" />

                                    {errors.username && <p style={{ color: 'red', fontSize: 'smaller' }}>{errors.username.message}</p>}
                                </Form.Group>


                                <Form.Group className="mb-3" controlId="formBasicEmail">
                                    <Form.Label>Email</Form.Label>
                                    <Form.Control
                                        type="email"
                                        {...register("email", { required: "email is required", })}
                                        placeholder="Email" />
                                    {errors.email && <p style={{ color: 'red', fontSize: 'smaller' }}>{errors.email.message}</p>}
                                </Form.Group>

                                <Form.Group className="mb-3" controlId="formBasicPassword">
                                    <Form.Label>Password</Form.Label>
                                    <Form.Control
                                        type="password"
                                        {...register("password", { required: "password is required" })}
                                        placeholder="Password" />

                                    {errors.password && <p style={{ color: 'red', fontSize: 'smaller' }}>{errors.password.message}</p>}
                                </Form.Group>
                            </Col>
                            <Col >
                                <Form.Group className="mb-3" controlId="formBasicMobile">
                                    <Form.Label>Mobile</Form.Label>
                                    <Form.Control
                                        type="number"
                                        {...register("mobile", { required: 'mobile number is required' })}
                                        placeholder="Mobile" />

                                    {errors.mobile && <p style={{ color: 'red', fontSize: 'smaller' }}>{errors.mobile.message}</p>}
                                </Form.Group>

                                <Form.Group className="mb-3" controlId="formBasicAge">
                                    <Form.Label>Age</Form.Label>
                                    <Form.Control
                                        type="number"
                                        {...register("age", { required: "Age is required" })}
                                        placeholder="age" />
                                    {errors.age && <p style={{ color: 'red', fontSize: 'smaller' }}>{errors.age.message}</p>}
                                </Form.Group>

                                <Form.Group className="mb-3" controlId="formBasicHeight">
                                    <Form.Label>Height</Form.Label>
                                    <Form.Control
                                        type="number"
                                        {...register("height", { required: "height is required" })}
                                        placeholder="Height" />
                                    {errors.height && <p style={{ color: 'red', fontSize: 'smaller' }}>{errors.height.message}</p>}
                                </Form.Group>

                                <Form.Group className="mb-3" controlId="formBasicWeight">
                                    <Form.Label>Weight</Form.Label>
                                    <Form.Control
                                        type="number"
                                        {...register("weight", { required: "weight is required" })}
                                        placeholder="Weight" />
                                    {errors.weight && <p style={{ color: 'red', fontSize: 'smaller' }}>{errors.weight.message}</p>}
                                </Form.Group>

                            </Col>


                        </Row>


                        <button type="submit" className='submit_button' >
                            Submit
                        </button>

                    </Form>
                </div>

            </Row>
        </Container>

    )
}
