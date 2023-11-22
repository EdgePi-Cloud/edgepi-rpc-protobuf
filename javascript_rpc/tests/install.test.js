const os = require("os");
const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");
const protobuf = require("protobufjs");
const findRoot = require("find-root");

describe("Protobuf Installation Integration Test", () => {
  test("testProtobufInstallation", async () => {
    // Create a unique directory in the os's temporary directory
    const tempDir = os.tmpdir();
    const uniqueDir = path.join(tempDir, `${Date.now()}`);
    fs.mkdirSync(uniqueDir);

    try {
      repoRoot = path.join(findRoot(__dirname), "..");
      const protoFiles = fs
        .readdirSync(repoRoot)
        .filter((file) => file.endsWith(".proto"));
      protoFiles.forEach((file) => {
        const sourcePath = path.join(repoRoot, file);
        const destPath = path.join(uniqueDir, file);
        fs.copyFileSync(sourcePath, destPath);
      });

      execSync(`npm install ${findRoot(__dirname)}`, { cwd: uniqueDir });

      const root = await protobuf.load(path.join(uniqueDir, "pwm.proto"));
      const GetFrequency = root.lookupType("GetFrequency");

      const pwmMsg = GetFrequency.create({ frequency: 2000 });
      const buffer = GetFrequency.encode(pwmMsg).finish();
      const decodedMsg = GetFrequency.decode(buffer);

      expect(decodedMsg.frequency).toBe(2000);
    } catch (error) {
      throw error;
    } finally {
      fs.rmSync(uniqueDir, { recursive: true });
    }
  });
});
