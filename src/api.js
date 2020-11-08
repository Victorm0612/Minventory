import axios from 'axios';
import store from "./store";

function getUsers(id) {
    return axios.get('user/' + id, {
            headers: {
                "Authorization": 'Token ' + store.getters.retrieveToken,
            }
        })
        .catch((error) => {
            console.log("Error when getting users: " + error);
        })
}

function createUser(user) {
    return axios.post('register/', {
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

function updateUser(user) {
    return axios.put('user/' + store.getters.retrieveId + '/', {
            headers: {
                "Authorization": 'Token ' + store.getters.retrieveToken,
            }
        }, {
            name: user.getName(),
            last_name: user.getLastName(),
            document_number: user.getDocumentNumber(),
            phone: user.getPhone(),
            email: user.getEmail(),
            password: user.getPassword(),
            address: user.getAddress(),
            gender: user.getGender(),
            type: user.getType()
        })
        .then(res => console.log(res))
}

function createRequestQuotation(request_quotation) {
    return axios.post('quotation/', {
            scheduled_date: request_quotation.getScheduledDate(),
            time_range: request_quotation.getTimeRange(),
            approved: request_quotation.getApproved(),
            service_type: request_quotation.getServiceType(),
            description: request_quotation.getDescription(),
            fkUser_id: request_quotation.getUser()
        })
        .then(response => response)
        .catch((error) => {
            if (error.response) {
                return error.response;
            }
        })
}

export default {
    getUsers,
    createUser,
    createRequestQuotation,
    updateUser,
}