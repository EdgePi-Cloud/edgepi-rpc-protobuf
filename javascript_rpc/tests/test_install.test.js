const os = require("os");
const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");
const protobuf = require("protobufjs");
const findRoot = require("find-root");

describe("Protobuf Installation Integration Test", () => {
  test("testProtobufInstallation", async () => {
    // Using the os's default temporary directory
    const tempDir = os.tmpdir();

    try {
      // findRoot gets the nearest package.json, so repoRoot will get the repository root
      repoRoot = path.join(findRoot(__dirname), "..");
      const protoFiles = fs
        .readdirSync(repoRoot)
        .filter((file) => file.endsWith(".proto"));
      protoFiles.forEach((file) => {
        const sourcePath = path.join(repoRoot, file);
        const destPath = path.join(tempDir, file);

        fs.copyFileSync(sourcePath, destPath);
      });

      // Install the npm module in the temporary directory
      execSync(`npm install ${findRoot(__dirname)}`, { cwd: tempDir });

      // Load and test protobuf
      const root = await protobuf.load(path.join(tempDir, "pwm.proto"));
      const GetFrequency = root.lookupType("GetFrequency");

      // Test serialization/deserialization
      const pwmMsg = GetFrequency.create({ frequency: 2000 });
      const buffer = GetFrequency.encode(pwmMsg).finish();
      const decodedMsg = GetFrequency.decode(buffer);

      expect(decodedMsg.frequency).toBe(2000);
    } catch (error) {
      throw error;
    } finally {
      // Remove temporary directory
      fs.rmSync(tempDir, { recursive: true });
    }
  });
});
