import axios from 'axios';
import store from "./store";


function getUsers(id) {
    return axios.get('user/' + id, {
            headers: {
                "Authorization": 'Token ' + store.getters.retrieveUser.token,
            }
        })
        .catch((error) => {
            console.log("Error while get user: " + error)
        })
}

function createUser(user) {
    return axios.post('register/', {
        name: user.getName(),
        last_name: user.getLastName(),
        document_type: user.getDocumentType(),
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
    return axios.put('user/' + store.getters.retrieveUser.id_user + '/', {
            avatar: user.getAvatar(),
            name: user.getName(),
            last_name: user.getLastName(),
            document_type: user.getDocumentType(),
            document_number: user.getDocumentNumber(),
            phone: user.getPhone(),
            email: user.getEmail(),
            password: user.getPassword(),
            address: user.getAddress(),
            gender: user.getGender(),
            type: user.getType()
        }, {
            headers: {
                "Authorization": 'Token ' + store.getters.retrieveUser.token,
            }
        })
        .catch((error) => {
            console.log("Error while update user: " + error)
        })
}

function createRequestQuotation(request_quotation) {
    return axios.post('quotation/', {
            scheduled_date: request_quotation.getScheduledDate(),
            time_range: request_quotation.getTimeRange(),
            approved: request_quotation.getApproved(),
            service_type: request_quotation.getServiceType(),
            description: request_quotation.getDescription(),
            fkUser_id: request_quotation.getUser()
        }, {
            headers: {
                "Authorization": 'Token ' + store.getters.retrieveUser.token,
            }
        })
        .then(response => response)
        .catch((error) => {
            if (error.response) {
                return error.response;
            }
        })
}

function getQuotationsByID() {
    return axios.get('quotation/user-quotation/' + store.getters.retrieveUser.id_user, {
            headers: {
                "Authorization": 'Token ' + store.getters.retrieveUser.token,
            }
        })
        .then(response => response)
        .catch((error) => {
            if (error.response) {
                return error.response;
            }
        })
}

function updateQuotationByID(id, request_quotation, scheduled_date) {
    return axios.put('quotation/' + id + '/', {
            scheduled_date: scheduled_date,
            time_range: request_quotation.getTimeRange(),
            approved: request_quotation.getApproved(),
            service_type: request_quotation.getServiceType(),
            description: request_quotation.getDescription(),
            fkUser_id: request_quotation.getUser()
        }, {
            headers: {
                "Authorization": 'Token ' + store.getters.retrieveUser.token,
            }
        })
        .then(response => response)
        .catch((error) => {
            if (error.response) {
                return error.response;
            }
        })
}

function deleteQuotationByID(id) {
    return axios.delete('quotation/' + id + '/', {
            headers: {
                "Authorization": 'Token ' + store.getters.retrieveUser.token,
            }
        })
        .then(response => response)
        .catch((error) => {
            if (error.response) {
                return error.response;
            }
        })
}

function getTaskEmployee(id) {
    return axios.get('task/employee-task/' + id, {
            headers: {
                "Authorization": 'Token ' + store.getters.retrieveUser.token,
            }
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
    getQuotationsByID,
    updateQuotationByID,
    deleteQuotationByID,
    getTaskEmployee
}