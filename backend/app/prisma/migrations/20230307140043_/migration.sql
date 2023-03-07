-- CreateTable
CREATE TABLE "User" (
    "id" SERIAL NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,
    "firstName" TEXT NOT NULL,
    "lastName" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "dateOfBirth" TIMESTAMP(3),
    "profileImage" TEXT,
    "addressOne" TEXT,
    "addressTwo" TEXT,
    "zipCode" TEXT,
    "phoneNumer" TEXT,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);
