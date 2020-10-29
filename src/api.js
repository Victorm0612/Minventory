import axios from 'axios'

function getUsers() {
    return axios
        .get('user/')
        .then(response => response.data)
        .catch((error) => {
            console.log("Error when getting users: " + error);
        })
}

function createUser(user) {
    return axios.post('user/', {
        name: user.getName(),
        last_name: user.getLastName(),
        document_number: user.getDocumentNumber(),
        phone: user.getPhone(),
        email: user.getEmail(),
        password: user.getPassword(),
        address: user.getAddress(),
        gender: user.getGender(),
        type: user.getType()
    }).catch((error) => {
        console.log("Error while creating user: " + error);
    })
}

export default {
    getUsers,
    createUser,
}