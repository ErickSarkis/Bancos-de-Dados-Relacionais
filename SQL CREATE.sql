-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8mb3 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`funcionários`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`funcionários` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NULL DEFAULT NULL,
  `Cargo` VARCHAR(45) NULL DEFAULT NULL,
  `Departamento` VARCHAR(45) NULL DEFAULT NULL,
  `Salario` DECIMAL(10,2) NULL DEFAULT NULL,
  `Data_contratacao` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB
AUTO_INCREMENT = 24
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`hardware`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`hardware` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `hardware` VARCHAR(45) NULL DEFAULT NULL,
  `modelo` VARCHAR(45) NULL DEFAULT NULL,
  `quantidade` INT NULL DEFAULT NULL,
  `preco` DECIMAL(10,2) NULL DEFAULT NULL,
  `total_preco` DECIMAL(10,2) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`funcionarios_hardwares`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`funcionarios_hardwares` (
  `ID_Funcionario` INT NOT NULL,
  `ID_Hardware` INT NOT NULL,
  PRIMARY KEY (`ID_Funcionario`, `ID_Hardware`),
  CONSTRAINT `funcionarios_hardwares_ibfk_1`
    FOREIGN KEY (`ID_Funcionario`)
    REFERENCES `mydb`.`funcionários` (`ID`),
  CONSTRAINT `funcionarios_hardwares_ibfk_2`
    FOREIGN KEY (`ID_Hardware`)
    REFERENCES `mydb`.`hardware` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

CREATE INDEX `ID_Hardware` ON `mydb`.`funcionarios_hardwares` (`ID_Hardware` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `mydb`.`perifericos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`perifericos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `periferico` VARCHAR(255) NULL DEFAULT NULL,
  `modelo` VARCHAR(255) NULL DEFAULT NULL,
  `quantidade` INT NULL DEFAULT NULL,
  `preco` DECIMAL(10,3) NULL DEFAULT NULL,
  `preco_total` DECIMAL(10,3) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`funcionarios_perifericos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`funcionarios_perifericos` (
  `ID_Funcionario` INT NOT NULL,
  `ID_Periferico` INT NOT NULL,
  PRIMARY KEY (`ID_Funcionario`, `ID_Periferico`),
  CONSTRAINT `funcionarios_perifericos_ibfk_1`
    FOREIGN KEY (`ID_Funcionario`)
    REFERENCES `mydb`.`funcionários` (`ID`),
  CONSTRAINT `funcionarios_perifericos_ibfk_2`
    FOREIGN KEY (`ID_Periferico`)
    REFERENCES `mydb`.`perifericos` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

CREATE INDEX `ID_Periferico` ON `mydb`.`funcionarios_perifericos` (`ID_Periferico` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `mydb`.`softwares`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`softwares` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `licenca` VARCHAR(45) NULL DEFAULT NULL,
  `quantidade` INT NULL DEFAULT NULL,
  `preco` DECIMAL(10,3) NULL DEFAULT NULL,
  `preco_total` DECIMAL(10,3) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`funcionarios_softwares`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`funcionarios_softwares` (
  `ID_Funcionario` INT NOT NULL,
  `ID_Software` INT NOT NULL,
  PRIMARY KEY (`ID_Funcionario`, `ID_Software`),
  CONSTRAINT `funcionarios_softwares_ibfk_1`
    FOREIGN KEY (`ID_Funcionario`)
    REFERENCES `mydb`.`funcionários` (`ID`),
  CONSTRAINT `funcionarios_softwares_ibfk_2`
    FOREIGN KEY (`ID_Software`)
    REFERENCES `mydb`.`softwares` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

CREATE INDEX `ID_Software` ON `mydb`.`funcionarios_softwares` (`ID_Software` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `mydb`.`servidores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`servidores` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL DEFAULT NULL,
  `so` VARCHAR(45) NULL DEFAULT NULL,
  `armazenamento_tb` DECIMAL(5,2) NULL DEFAULT NULL,
  `data_instalacao` DATE NULL DEFAULT NULL,
  `custo_manutencao` DECIMAL(5,2) NULL DEFAULT NULL,
  `status_servidor` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
