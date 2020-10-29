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
}