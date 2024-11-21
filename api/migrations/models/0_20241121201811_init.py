from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `user_info` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '主键',
    `username` VARCHAR(32) NOT NULL UNIQUE COMMENT '用户名',
    `nickname` VARCHAR(32) NOT NULL  COMMENT '昵称',
    `password` VARCHAR(128) NOT NULL  COMMENT '密码',
    `openid` VARCHAR(128) NOT NULL UNIQUE COMMENT '微信openid',
    `avatar` VARCHAR(256) NOT NULL  COMMENT '头像',
    `status` INT NOT NULL  COMMENT '状态' DEFAULT 1,
    `mobile` VARCHAR(11) NOT NULL UNIQUE COMMENT '手机号',
    `email` VARCHAR(64) NOT NULL UNIQUE COMMENT '邮箱',
    `country` VARCHAR(32) NOT NULL  COMMENT '国家',
    `province` VARCHAR(32) NOT NULL  COMMENT '省份',
    `city` VARCHAR(32) NOT NULL  COMMENT '城市',
    `gender` INT NOT NULL  COMMENT '性别' DEFAULT 0,
    `created_at` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6)   COMMENT '删除时间',
    KEY `idx_user_info_nicknam_a9d217` (`nickname`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
