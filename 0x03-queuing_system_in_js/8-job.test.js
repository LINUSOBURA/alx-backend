import { expect } from "chai";
import kue from "kue";
import createPushNotificationsJobs from "./8-job.js";

describe("createPushNotificationsJobs", () => {
  let queue;

  beforeEach(() => {
    // Create a queue and enter test mode
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    // Clear the queue and exit test mode
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it("should throw an error if jobs is not an array", () => {
    expect(() => createPushNotificationsJobs("not an array", queue)).to.throw(
      "Jobs is not an array"
    );
  });

  it("should create jobs in the queue with correct data", () => {
    const jobs = [
      { phoneNumber: "1234567890", message: "Hello, this is job 1" },
      { phoneNumber: "0987654321", message: "Hello, this is job 2" },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal("push_notification_code_3");
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].type).to.equal("push_notification_code_3");
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });

  it("should log correct messages when jobs are processed", () => {
    const jobs = [
      { phoneNumber: "1234567890", message: "Hello, this is job 1" },
    ];

    createPushNotificationsJobs(jobs, queue);

    const job = queue.testMode.jobs[0];

    job.on("complete", () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on("failed", (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    job.on("progress", (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    // Simulate job events
    job._events.complete();
    job._events.failed(new Error("Test error"));
    job._events.progress(50);
  });
});
