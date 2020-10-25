import axios from 'axios'

const url = 'http://localhost:8000/api/user/'

function getUsers() {
    return axios
        .get(url)
        .then(response => response.data)
        .catch((error) => {
            console.log("Error when getting users: " + error);
        })
}

function createUser() {
    return axios({
        method: 'post',
        url: url,
        data: {
            name: "victor",
            last_name: "Janse",
            document_number: 1185530787,
            phone: 3166365487,
            email: "ejemplo@ejemplo.com",
            password: "aaaA1235#",
            address: "some address",
            gender: "femenino",
            type: 2
        }
    }).catch((error) => {
        console.log("Error while creating user: " + error);
        console.log(this.data)
    })
}

export default {
    getUsers,
    createUser,
}