export default class RequestQuotation {
    ScheduledDate = null;
    TimeRange = null;
    Approved = null;
    ServiceType = null;
    Description = null;
    User = null;
    
    constructor(scheduled_date, time_range, approved, service_type, description, user) {
        this.ScheduledDate = scheduled_date;
        this.TimeRange = time_range;
        this.Approved = approved;
        this.ServiceType = service_type;
        this.Description = description;
        this.User = user;
    }

    getScheduledDate() {
        return this.ScheduledDate
    }
    getTimeRange() {
        return this.TimeRange
    }
    getApproved() {
        return this.Approved
    }
    getServiceType() {
        return this.ServiceType
    }
    getDescription() {
        return this.Description
    }
    getUser() {
        return this.User
    }
}