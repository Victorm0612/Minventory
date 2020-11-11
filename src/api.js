import axios from 'axios';
import store from "./store";


function getUsers(id) {
    return axios.get('user/' + id, {
            headers: {
                "Authorization": 'Token ' + store.getters.retrieveToken,
            }
        })
        .catch((error) => {
            if (error.response.status === 403 && error.response.data.detail === 'access_token expired') {
                store.dispatch('destroyToken')
            } else {
                console.log('parece otra cosa')
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
    }).catch((error) => {
        console.log("Error while creating user: " + error);
    })
}

function updateUser(user) {
    return axios.put('user/' + store.getters.retrieveId + '/', {
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
                "Authorization": 'Token ' + store.getters.retrieveToken,
            }
        })
        .then(res => console.log(res))
        .catch((error) => {
            if (error.response.status === 403 && error.response.data.detail === 'access_token expired') {
                store.dispatch('destroyToken')
            } else {
                console.log('parece otra cosa')
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