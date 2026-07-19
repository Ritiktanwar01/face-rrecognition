const mongoose = require("mongoose")
const env = require("dotenv")
const {serverLogger} = require("./logger")

env.config()


const ConnectDB = async()=>{
    try {
        mongoose.connect(process.env.MONGODBURI)
        serverLogger.info("server started")
    } catch (error) {
        serverLogger.error(error.message)
    }
}

module.exports = { ConnectDB }