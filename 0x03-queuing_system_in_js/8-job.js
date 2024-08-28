import kue from "kue";

function createPushNotificationsJobs(jobs, queue) {
  // Check if the input 'jobs' is an array
  if (!Array.isArray(jobs)) {
    throw new Error("Jobs is not an array");
  }

  // Loop through each job in the jobs array
  jobs.forEach((jobData) => {
    // Create a job in the queue 'push_notification_code_3'
    const job = queue
      .create("push_notification_code_3", jobData)
      .save((err) => {
        if (!err) {
          console.log(`Notification job created: ${job.id}`);
        }
      });

    // Handle job completion
    job.on("complete", () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Handle job failure
    job.on("failed", (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    // Handle job progress
    job.on("progress", (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
