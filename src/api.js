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

function getUsersByType(type) {
    return axios.get('user/by-type/' + type, {
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
        })
        .then(response => response)
        .catch((error) => {
            if (error.response) {
                return error.response;
            }
        })
}

function updateUser(id, user) {
    return axios.put('user/' + id + '/', {
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
        .then(response => response)
        .catch((error) => {
            if (error.response) {
                return error.response;
            }
        })
}

function deleteUser(id) {
    return axios.delete('user/' + id + '/', {
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

function getTasks(uri) {
    return axios.get(uri, {
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

function getBillByType(type) {
    return axios.get('bill/by-type/' + type, {
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

function createExpense(bill) {
    return axios.post('bill/', {
            bill_type: bill.getBillType(),
            total_price: bill.getTotalPrice(),
            description: bill.getDescription(),
            fkTask: bill.getFkTask()
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

function updateBillByID(id, bill) {
    return axios.put('bill/' + id + '/', {
            bill_type: bill.getBillType(),
            total_price: bill.getTotalPrice(),
            description: bill.getDescription()
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

function deleteBillByID(id) {
    return axios.delete('bill/' + id + '/', {
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
    getTasks,
    getUsersByType,
    deleteUser,
    getBillByType,
    createExpense,
    updateBillByID,
    deleteBillByID
}