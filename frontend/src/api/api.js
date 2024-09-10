import axios from 'axios';


const apiClient = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
    timeout: 1000,
    headers: {
        'Content-Type': 'application/json',
    }
})


export function login(username, password) {
    return apiClient.post('/api/users/login', {
        'username': username, 'password': password
    })
}

export function getUser(token) {
    return apiClient.get('/api/users/me',{
        headers: {
            Authorization: 'Token ' + token
        }
    })
}

export function logout(token) {
    return apiClient.post('/api/users/logout', {}, {
        headers: {
            Authorization: 'Token ' + token
        }
    });
}

export function allGroups(token) {
    return apiClient.get('/api/groups', {
        headers: {
            Authorization: 'Token ' + token
        }
    })
}


export function studentsByGroup(token, group_id) {
    return apiClient.get('/api/users/student/all?group_id=' + group_id, {
        headers: {
            Authorization: 'Token ' + token
        }
    })
}

export async function subjectsByCourse(token, group_id) {

    const course = await apiClient.get('/api/groups/' + group_id, {
        headers: {
            Authorization: 'Token ' + token
        }
    }).then(response => response.data.course);

    return apiClient.get('/api/subject?course=' + course, {
        headers: {
            Authorization: 'Token ' + token
        }
    })
}


export function addGrade(grade, theme, student_id, subject_id, date) {
    return apiClient.post('/api/grades/create', {
        "grade": grade,
        "theme": theme,
        "student": student_id,
        "subject": subject_id,
        "date": date
    },{
        headers: {
            Authorization: 'Token ' + localStorage.getItem("token")
        }
    })
}
