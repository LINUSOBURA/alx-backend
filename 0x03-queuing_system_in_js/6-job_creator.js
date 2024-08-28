import kue from "kue";

const queue = kue.createQueue();

const jobData = {
  phoneNumber: "123456789",
  message: "This is the code 1234 to verify your account",
};

const job = queue.create("push_notification_code", jobData).save((err) => {
  if (!err) {
    console.log(`Notification Job created: ${job.id}`);
  } else {
    console.log("Error creating job", err);
  }
});

job.on("complete", () => {
  console.log("Notification job completed");
});

job.on("failed", () => {
  console.log("Notification job failed");
});
