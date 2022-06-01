// // import React from 'react'
// // import { Navbar, Nav, Container, Row, Col } from 'react-bootstrap'


// // export const Header = () => {
// //     return (
// //         <div>
// //             <Navbar bg="light" expand="lg">
// //                 <Container>

// //                     <Navbar.Brand ><span style={{ color: 'green', fontWeight: 'bold', textShadow: '1px 1px 3px green' }} >Health</span><span style={{ fontWeight: 'bold', textShadow: '1px 1px 3px black' }}>Coach</span></Navbar.Brand>


// //                     <Navbar.Toggle aria-controls="basic-navbar-nav" />
// //                     <Navbar.Collapse id="basic-navbar-nav">
// //                         <Nav className="me-auto " >

// //                             <Nav.Link >Home</Nav.Link>
// //                             <Nav.Link >Free Workouts</Nav.Link>
// //                             <Nav.Link >Programs</Nav.Link>
// //                             <Nav.Link >About</Nav.Link>
// //                             <div style={{ height: '50px', width: '50px', borderRadius: '50px', backgroundColor: 'whitesmoke', boxShadow: ' rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset' }}></div>
// //                             <Nav.Link >Signup</Nav.Link>
// //                             <Nav.Link >Login</Nav.Link>

// //                         </Nav>
// //                     </Navbar.Collapse>

// //                 </Container>
// //             </Navbar>
// //         </div>
// //     )
// // }




import MenuIcon from '@mui/icons-material/Menu';
import AppBar from '@mui/material/AppBar';
import Avatar from '@mui/material/Avatar';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuItem from '@mui/material/MenuItem';
import Menu from '@mui/material/Menu';
import Toolbar from '@mui/material/Toolbar';
import Tooltip from '@mui/material/Tooltip';
import Typography from '@mui/material/Typography';
import React, { useEffect, useState, } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Navbar, Nav, Container, Row, Col } from 'react-bootstrap'
import jwt_decode from "jwt-decode";
import { FREE_WORKOUTS, PROGRAMS, ABOUT } from '../../Constants/UserConstants'
import './Header.css';


const Header = () => {


    const token = localStorage.getItem("userAccessToken")


    const [Err, setErrors] = useState()
    const navigate = useNavigate()
    const [log, setLog] = useState(false)

    // try {
    //     const decode = jwt_decode(token.username)
    //     console.log(decode.username);

    // }

    // catch (Err) {
    //     setErrors("dijkfs")
    // }
    // const decode = jwt_decode(token.username)
    // console.log(decode);


    // useEffect(() => {



    //     if (token) {

    //         const decode = jwt_decode(token.username)
    //         console.log(decode);

    //     }

    // }, [])


    //logout fuction
    const logout = () => {


        navigate('/login')

    };

    // const decode = jwt_decode(token.username)
    // console.log(decode)

    const [anchorElNav, setAnchorElNav] = React.useState(null);
    const [anchorElUser, setAnchorElUser] = React.useState(null);

    const handleOpenNavMenu = (event) => {
        setAnchorElNav(event.currentTarget);
    };
    const handleOpenUserMenu = (event) => {
        setAnchorElUser(event.currentTarget);
    };

    const handleCloseNavMenu = () => {
        setAnchorElNav(null);
    };

    const handleCloseUserMenu = () => {
        setAnchorElUser(null);
    };

    return (
        < AppBar className='main_header' position="static" >

            <Toolbar className='header mx-5' disableGutters>
                <Typography
                    variant="h6"
                    noWrap
                    component="div"
                    sx={{ mr: 2, display: { xs: 'none', md: 'flex' } }}
                >
                    <Navbar.Brand ><span style={{ color: 'green', fontWeight: 'bold', textShadow: '1px 1px 3px green', fontSize: 'larger' }} >Health</span><span style={{ fontWeight: 'bold', textShadow: '1px 1px 3px black', fontSize: 'larger' }}>Coach</span></Navbar.Brand>

                </Typography>

                <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}>
                    <IconButton
                        size="large"
                        aria-label="account of current user"
                        aria-controls="menu-appbar"
                        aria-haspopup="true"
                        onClick={handleOpenNavMenu}
                        color="inherit"
                    >
                        <MenuIcon />
                    </IconButton>
                    <Menu
                        id="menu-appbar"
                        anchorEl={anchorElNav}
                        anchorOrigin={{
                            vertical: 'bottom',
                            horizontal: 'left',
                        }}
                        keepMounted
                        transformOrigin={{
                            vertical: 'top',
                            horizontal: 'left',
                        }}
                        open={Boolean(anchorElNav)}
                        onClose={handleCloseNavMenu}
                        sx={{
                            display: { xs: 'block', md: 'none' },
                        }}
                    >

                        <MenuItem style={{ display: "flex", flexDirection: "column" }} onClick={handleCloseNavMenu}>
                            <Button

                                onClick={handleCloseNavMenu}
                                sx={{ my: 2, color: 'black', display: 'block' }}
                            >
                                {FREE_WORKOUTS}
                            </Button>
                            <Link style={{ textDecorationLine: 'none' }} to={'/programs'}>  <Button

                                onClick={handleCloseNavMenu}
                                sx={{ my: 2, color: 'black', display: 'block' }}
                            >
                                {PROGRAMS}
                            </Button></Link>
                            <Link style={{ textDecorationLine: 'none' }} to={'/workout'}>      <Button

                                onClick={handleCloseNavMenu}
                                sx={{ my: 2, color: 'black', display: 'block' }}
                            >
                                {ABOUT}
                            </Button>       </Link>




                        </MenuItem>

                    </Menu>
                </Box>
                <Typography
                    variant="h6"
                    noWrap
                    component="div"
                    sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}
                >
                    Health Coach
                </Typography>
                <Box sx={{ justifyContent: 'center', flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>

                    <Button

                        onClick={handleCloseNavMenu}
                        sx={{ my: 2, color: 'black', display: 'block' }}
                    >
                        {FREE_WORKOUTS}
                    </Button>
                    <Link style={{ textDecorationLine: 'none' }} to={'/programs'}>
                        <Button

                            onClick={handleCloseNavMenu}
                            sx={{ my: 2, color: 'black', display: 'block' }}
                        >
                            {PROGRAMS}
                        </Button>
                    </Link>
                    <Link style={{ textDecorationLine: 'none' }} to={'/workout'}>
                        <Button

                            onClick={handleCloseNavMenu}
                            sx={{ my: 2, color: 'black', display: 'block' }}>
                            {ABOUT}
                        </Button>
                    </Link>


                    <Link to={'/trainerlogin'} style={{ textDecorationLine: "none" }}><Button

                        onClick={handleCloseNavMenu}
                        sx={{ my: 2, color: 'black', display: 'block' }}
                    >

                    </Button></Link>


                </Box>
                {token && <Typography className='username'>{token.username}</Typography>}
                {!token && <Link to={'/login'} style={{ textDecorationLine: 'none' }} >
                    <Button sx={{ marginRight: "9px" }} variant="outlined" >
                        Login
                    </Button>
                </Link>}
                {!token && <Link to={'/signup'} style={{ textDecorationLine: 'none' }}>
                    <Button sx={{ marginRight: "9px" }} variant="outlined" >
                        Signup
                    </Button>
                </Link>}



                <Box sx={{ flexGrow: 0 }}>
                    {token && <Tooltip title="Open settings">

                        <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                            <Avatar alt="" src="" />
                        </IconButton>
                    </Tooltip>}
                    <Menu
                        sx={{ mt: '45px' }}
                        id="menu-appbar"
                        anchorEl={anchorElUser}
                        anchorOrigin={{
                            vertical: 'top',
                            horizontal: 'right',
                        }}
                        keepMounted
                        transformOrigin={{
                            vertical: 'top',
                            horizontal: 'right',
                        }}
                        open={Boolean(anchorElUser)}
                        onClose={handleCloseUserMenu}
                    >
                        <MenuItem onClick={handleCloseUserMenu}>
                            <Link style={{ textDecoration: 'none', color: 'black' }} to={'/myprofile'}><Typography textAlign="center">My Profile</Typography></Link>

                        </MenuItem>
                        <MenuItem onClick={handleCloseUserMenu}>
                            <Link style={{ textDecoration: 'none', color: 'black' }} to={'/myworkouts'}><Typography textAlign="center">My Workouts</Typography></Link>

                        </MenuItem>
                        <MenuItem onClick={handleCloseUserMenu}>
                            <Typography onClick={logout} textAlign="center">Logout</Typography>

                        </MenuItem>


                    </Menu>
                </Box>

            </Toolbar>
        </AppBar >
    );
};
export default Header;
