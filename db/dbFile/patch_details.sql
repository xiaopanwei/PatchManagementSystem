/*
 Navicat Premium Data Transfer

 Source Server         : 123
 Source Server Type    : MySQL
 Source Server Version : 80018
 Source Host           : rm-bp1ns8gwl0a1ihnyzro.mysql.rds.aliyuncs.com:3306
 Source Schema         : xpw_patch

 Target Server Type    : MySQL
 Target Server Version : 80018
 File Encoding         : 65001

 Date: 02/06/2021 22:15:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for patch_details
-- ----------------------------
DROP TABLE IF EXISTS `patch_details`;
CREATE TABLE `patch_details`  (
  `patch_id` int(255) NOT NULL AUTO_INCREMENT,
  `belong_app_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `belong_app_version_code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `patch_download_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `patch_content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `upload_time` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `download_state` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '0 未下发 1 已下发 2 已暂停',
  `patch_version` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `patch_size` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `patch_flag` int(255) NULL DEFAULT 0,
  PRIMARY KEY (`patch_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
