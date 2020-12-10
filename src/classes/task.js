export default class Task {
    ApprovedDate = null;
    RealizationDate = null;
    AssignmentWorker = null;
    FkRequestQuotation = null;
    FkTaskStatus = null;
    TypeTask = null;

    constructor(approvedDate, realizationDate, fkAssignmentWorker, fkRequestQuotation, fkTaskStatus, typeTask) {
        this.ApprovedDate = approvedDate;
        this.RealizationDate = realizationDate;
        this.AssignmentWorker = fkAssignmentWorker;
        this.FkRequestQuotation = fkRequestQuotation;
        this.FkTaskStatus = fkTaskStatus;
        this.TypeTask = typeTask;
    }

    getApprovedDate() {
        return this.ApprovedDate
    }
    getRealizationDate() {
        return this.RealizationDate
    }
    getAssignmentWorker() {
        return this.AssignmentWorker
    }
    getFkRequestQuotation() {
        return this.FkRequestQuotation
    }
    getFkTaskStatus() {
        return this.FkTaskStatus
    }
    getTypeTask() {
        return this.TypeTask
    }
}