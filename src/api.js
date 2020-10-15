import axios from 'axios'

const url = 'http://localhost:8000/user/'

function getUsers() {
    return  axios
        .get(url)
        .then(response => response.data)
        .catch((error) => {
            console.log("Error when getting users: "+error);
        })
}

/*function getServerByDomain(domain) {
    return  axios
        .get(`${url}/${domain}`)
        .then(response => response.data)
        .catch((error) => {
            console.log("this error: "+error);
        })
}*/

export default {
    getUsers,
}