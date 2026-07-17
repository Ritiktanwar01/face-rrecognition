const mongoose = require("mongoose")


const userSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true
    },
    employeeCode: {
        type: String,
        required: true
    },
    employeStatus: {
        type: String,
        enum: ["Active", "Inactive",]
    },
    photoPaths: {
        type: [String],
        validate: {
            validator: function (arr) {
                // Ensure array length is exactly 2
                return arr.length === 2;
            },
            message: 'You must provide exactly two photos',
        }
    },
    DateOfbirth: {
        type: Date,
        required: true
    }

})

const attendance = new mongoose.Schema({
    employe: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User'
    },
    date: {
        type: Date,
        required: true,
        set: (val) => {
            const d = new Date(val);
            d.setHours(0, 0, 0, 0);
            return d;
        },
    },
    entryTime: {
        type: Date,
        required: true
    },
    exitTime: {
        type: Date,
        required: false
    }
})


const User = mongoose.model('User', userSchema);
const Attendance = mongoose.model("Attendence", attendance)


module.exports = { User, Attendance };