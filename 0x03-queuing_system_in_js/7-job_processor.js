import kue from "kue";

const blacklistedNumbers = ["4153518780", "4153518781"];

const queue = kue.createQueue();

// Function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  // Track the initial progress of the job
  job.progress(0, 100);

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job if the phone number is blacklisted
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track the job's progress to 50%
  job.progress(50, 100);

  // Log the notification message
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );

  // Complete the job successfully
  done();
}

// Process the jobs from the queue
queue.process("push_notification_code_2", 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
