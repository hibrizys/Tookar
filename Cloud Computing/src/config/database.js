const mysql = require('mysql');
require('dotenv').config();

// Create a connection pool
const pool = mysql.createPool({
  connectionLimit: 10, // Adjust as needed
  host: process.env.DB_HOST, //
  user: process.env.DB_USER, //
  password: process.env.DB_PASS,
  database: process.env.DB_DATABASE,
});

// Test the database connection
pool.getConnection((err, connection) => {
  if (err) {
    console.error('Database connection error:', err);
  } else {
    console.log('Connected to the database');
    connection.release();
  }
});


// Make the database connection available in other modules (if needed)
module.exports = pool;